#!/usr/bin/env python3
"""
연도/학기/과목별 정리 폴더를 만들고, README 목차를 자동 갱신하는 스크립트.

사용법
------
# 1) 새 과목 추가 (폴더 + README + course.json 생성 후 목차 자동 갱신)
python3 scripts/course.py new --year 2027 --semester 1 \
    --code BIO2001.01-00 --name "생화학(1)" --prof 홍길동

#   옵션
#   --type 비교과            : 비교과 활동이면 지정 (기본값: 교과)
#   --folder 폴더이름        : 폴더명을 직접 지정 (기본값: 코드_과목명 자동 생성)
#   --extra 실험보고서 ...   : 기본 하위폴더 외에 추가할 폴더
#   --minimal                : 하위폴더 없이 README만 생성 (실기 과목 등)

# 2) 목차만 다시 만들기 (폴더를 손으로 옮기거나 course.json을 고친 뒤)
python3 scripts/course.py index

구조
----
<연도>/<N학기>/<교과|비교과>/<코드_과목명>/
    course.json   과목 메타데이터 (목차 생성용)
    README.md     과목 개요 + 주차별 요약 표
    수업요약/ 과제/ 시험대비/  (+ --extra 폴더)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SUBDIRS = ["수업요약", "과제", "시험대비"]  # 강의자료 원본은 private 리포에만 보관
SUBDIR_DESC = {
    "강의자료": "슬라이드·핸드아웃·수업계획서 (공개 리포라면 원본 대신 링크 권장)",
    "수업요약": "주차별 요약 노트 (`templates/주차요약_템플릿.md` 복사해서 사용)",
    "과제": "과제 제출본·피드백",
    "시험대비": "중간/기말 정리, 예상문제, 오답노트",
    "실험보고서": "주차별 실험 보고서",
    "프로젝트": "팀/개인 프로젝트 산출물",
}
TOTAL_WEEKS = 16
MIDTERM_WEEK, FINAL_WEEK = 8, 16
START, END = "<!-- INDEX:START -->", "<!-- INDEX:END -->"


# ---------------------------------------------------------------- helpers
def slugify(code: str, name: str) -> str:
    """'SED2103.01-00', 'LINEAR ALGEBRA' -> 'SED2103_Linear-Algebra'."""
    base = code.split(".")[0]
    clean = re.sub(r"\((\d+)\)", r"\1", name)          # 수영(1) -> 수영1
    clean = re.sub(r"[()\[\];:/\\]", " ", clean)
    words = clean.split()
    if all(w.isascii() for w in words):
        # 3글자 이하 대문자(ISE 등 약어)는 유지, 나머지는 Title case
        words = [w.capitalize() if w.isupper() and len(w.rstrip("0123456789")) > 3 else w
                 for w in words]
    return f"{base}_{'-'.join(words)}"


def sem_order(sem) -> float:
    """1학기 < 여름 < 2학기 < 겨울 순으로 정렬."""
    return {"1": 1, "여름": 1.5, "2": 2, "겨울": 2.5}.get(str(sem), 9)


def semester_label(year: int, sem: str) -> str:
    return f"{year}년 {sem}학기"


def write_if_missing(path: Path, text: str) -> None:
    if not path.exists():
        path.write_text(text, encoding="utf-8")


# ---------------------------------------------------------------- new
def course_readme(meta: dict, subdirs: list[str]) -> str:
    rows = []
    for w in range(1, TOTAL_WEEKS + 1):
        topic = "**중간고사**" if w == MIDTERM_WEEK else "**기말고사**" if w == FINAL_WEEK else ""
        rows.append(f"| {w} | {topic} | | |")
    folder_lines = "\n".join(
        f"- [`{d}/`](./{d}) — {SUBDIR_DESC.get(d, '')}" for d in subdirs
    ) or "- (실기 위주 과목 — 하위 폴더 없음)"
    return f"""# {meta['name']}

| 항목 | 내용 |
|---|---|
| 과목코드 | {meta['code']} |
| 담당교수 | {meta['prof']} |
| 학기 | {semester_label(meta['year'], meta['semester'])} |
| 구분 | {meta['type']} · 학부 |

## 📁 폴더 구성
{folder_lines}

## 📝 주차별 수업 요약
요약 노트를 `수업요약/`에 올린 뒤 아래 표에 링크를 걸어 주세요.

| 주차 | 주제 | 요약 노트 | 비고 |
|---|---|---|---|
{chr(10).join(rows)}

## 📌 과제 · 시험 기록
| 구분 | 내용 | 마감/일자 | 링크 |
|---|---|---|---|
| | | | |
"""


def cmd_new(a: argparse.Namespace) -> None:
    sem = str(a.semester)
    folder = a.folder or slugify(a.code, a.name)
    course_dir = ROOT / str(a.year) / f"{sem}학기" / a.type / folder
    if course_dir.exists():
        sys.exit(f"이미 존재합니다: {course_dir.relative_to(ROOT)}")

    subdirs = [] if a.minimal else DEFAULT_SUBDIRS + [e for e in a.extra if e not in DEFAULT_SUBDIRS]
    course_dir.mkdir(parents=True)
    for d in subdirs:
        (course_dir / d).mkdir()
        (course_dir / d / ".gitkeep").touch()

    meta = {
        "year": a.year, "semester": sem, "type": a.type,
        "code": a.code, "name": a.name, "prof": a.prof,
    }
    (course_dir / "course.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (course_dir / "README.md").write_text(course_readme(meta, subdirs), encoding="utf-8")
    print(f"생성: {course_dir.relative_to(ROOT)}")
    cmd_index(a)


# ---------------------------------------------------------------- index
def load_courses() -> list[tuple[Path, dict]]:
    out = []
    for f in ROOT.glob("[0-9][0-9][0-9][0-9]/*학기/*/*/course.json"):
        out.append((f.parent, json.loads(f.read_text(encoding="utf-8"))))
    type_order = {"교과": 0, "비교과": 1}
    out.sort(key=lambda x: (x[1]["year"], sem_order(x[1]["semester"]),
                            type_order.get(x[1]["type"], 9), x[1]["code"]))
    return out


def link(path: Path, base: Path) -> str:
    rel = path.relative_to(base).as_posix()
    return "./" + rel.replace(" ", "%20")


def course_table(courses, base: Path) -> str:
    lines = ["| 구분 | 과목코드 | 과목명 | 담당교수 |", "|---|---|---|---|"]
    for d, m in courses:
        lines.append(f"| {m['type']} | {m['code']} | [{m['name']}]({link(d, base)}) | {m['prof']} |")
    return "\n".join(lines)


def replace_block(path: Path, body: str) -> None:
    text = path.read_text(encoding="utf-8")
    if START not in text:
        text = text.rstrip() + f"\n\n{START}\n{END}\n"
    new = re.sub(re.escape(START) + r".*?" + re.escape(END),
                 f"{START}\n{body}\n{END}", text, flags=re.S)
    path.write_text(new, encoding="utf-8")


def cmd_index(_a=None) -> None:
    courses = load_courses()
    groups: dict[tuple[int, str], list] = {}
    for d, m in courses:
        groups.setdefault((m["year"], str(m["semester"])), []).append((d, m))

    # 학기 README
    for (year, sem), items in groups.items():
        sem_dir = ROOT / str(year) / f"{sem}학기"
        readme = sem_dir / "README.md"
        write_if_missing(readme, f"# {semester_label(year, sem)}\n\n"
                                 f"수강 과목 목록 (자동 생성 — `python3 scripts/course.py index`)\n")
        replace_block(readme, course_table(items, sem_dir))

    # 루트 README 목차
    parts = []
    for (year, sem), items in sorted(groups.items(), key=lambda g: (g[0][0], sem_order(g[0][1])), reverse=True):
        sem_dir = ROOT / str(year) / f"{sem}학기"
        parts.append(f"### 📅 [{semester_label(year, sem)}]({link(sem_dir, ROOT)}) — {len(items)}과목\n")
        parts.append(course_table(items, ROOT) + "\n")
    replace_block(ROOT / "README.md", "\n".join(parts).rstrip())
    print(f"목차 갱신: {len(courses)}과목 / {len(groups)}학기")


# ---------------------------------------------------------------- cli
def main() -> None:
    p = argparse.ArgumentParser(description="연도/학기/과목별 정리 폴더 관리")
    sub = p.add_subparsers(dest="cmd", required=True)

    n = sub.add_parser("new", help="새 과목 폴더 생성")
    n.add_argument("--year", type=int, required=True)
    n.add_argument("--semester", required=True, help="1, 2, 여름, 겨울 등")
    n.add_argument("--code", required=True, help="예: BIO1002.01-00")
    n.add_argument("--name", required=True, help="예: 일반생물학및실험(2)")
    n.add_argument("--prof", default="", help="담당교수")
    n.add_argument("--type", default="교과", choices=["교과", "비교과"])
    n.add_argument("--folder", help="폴더명 직접 지정")
    n.add_argument("--extra", nargs="*", default=[], help="추가 하위 폴더")
    n.add_argument("--minimal", action="store_true", help="하위 폴더 없이 생성")
    n.set_defaults(func=cmd_new)

    i = sub.add_parser("index", help="README 목차 재생성")
    i.set_defaults(func=cmd_index)

    a = p.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
