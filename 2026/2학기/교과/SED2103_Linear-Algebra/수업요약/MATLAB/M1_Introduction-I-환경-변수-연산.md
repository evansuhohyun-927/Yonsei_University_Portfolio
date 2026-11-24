# M1 Introduction I: 환경, 변수, 연산

Command Window에 바로 입력하고, = 로 값을 넣고, 연산자 우선순위대로 계산합니다. <sub>〔W1〕</sub> <sub>〔45:58〕</sub>

| 명령 | 하는 일 | 예 → 결과 | 함정 |
|---|---|---|---|
| `>>` prompt | 입력 즉시 실행 (interactive) | `3+4` → `ans = 7` | 식만 쓰면 결과가 `ans`에 덮어써집니다. |
| `pwd` `ls` `cd` | 현재 폴더 확인·목록·이동 | `cd Documents` | 스크립트·함수 파일은 현재 폴더나 path에 있어야 실행됩니다. |
| `=` | 오른쪽 값을 왼쪽 변수에 대입 | `mynum = mynum + 3` | 수학의 등호가 아닙니다. 오른쪽의 mynum이 먼저 있어야 합니다. |
| `;` | 출력만 숨김 | `x = 5;` | 계산과 저장은 그대로 됩니다. |
| `clc` `clear` | 화면 지우기 / 변수 삭제 | `clear x` | clc는 변수를 지우지 않습니다. |
| `who` `whos` | 변수 이름 / 이름·크기·class | `whos` | `namelengthmax` = 63자 |
| 변수명 | 문자로 시작, 문자·숫자·밑줄, 대소문자 구분 | `total_Score2` ✓, `2nd` ✕ | 하이픈은 빼기로 읽힙니다. 예약어(`for`, `end`) 불가 |
| `+ - * / ^` | 산술 연산 | `3+4*2^2` → 19 | 우선순위: () → ^ → 음수화 → \* / \\ → + − |
| `3e5` | scientific notation | `3e5` → 300000 | e는 자연상수가 아닙니다. |
| `format` | 표시 자릿수만 바꿈 | `format long`, `format rat` | 저장된 값은 바뀌지 않습니다. |
| `...` | 다음 줄로 이어 쓰기 | `x = 1 + 2 + ...` |   |
| `help` `doc` | 도움말 / 문서 창 | `help sin` | 연산자도 함수: `plus(2,5)` → 7 |

```matlab
x = 3 + 4*2^2        % 19
mynum = 5;
mynum = mynum + 3    % 8
b = 1 + 1i;          % double complex
whos                 % 이름, 크기, class
format long; pi      % 3.141592653589793
format short
```

<details>
<summary>📎 세션 시간표</summary>

Week 1 · 1주차 강의 비디오.mp4 / 1주차.mp3 / Week 1 - MATLAB SESSION.txt

|   |   |
|---|---|
| 00:53 | MATLAB을 쓰는 이유: accurate, fast, accessible(내장 함수와 라이브러리), mathematical, 시각화 우수. 데이터 → 처리 → 시각화 흐름. |
| 08:42 | Interactive: Command Window의 prompt `>>`에 입력하면 바로 결과가 나옵니다. 컴파일 언어의 코딩·컴파일·실행 단계가 필요 없습니다. |
| 10:47 | Layout: HOME → Layout. Current Folder, Workspace, Command Window, Command History. Toolstrip 탭은 HOME, PLOTS, APPS. |
| 13:17 | 현재 폴더: `pwd`, `ls`, `cd`. 함수 파일 작성 시 어느 폴더에 있는지가 중요합니다. |
| 16:02 | Workspace는 변수의 값, 크기, class를 보여 줍니다. `b = 1+1i`는 double complex. |
| 19:30 | Assignment: `=`는 수학의 등호가 아니라 오른쪽 값을 왼쪽 변수에 넣는 연산자입니다. |
| 22:19 | `clc` 화면 지우기, `clear` 변수 삭제. 세미콜론은 출력만 억제합니다. 식만 입력하면 `ans`에 저장됩니다. |
| 25:12 | `mynum = mynum + 3`은 값 갱신입니다. 초기화 없이 바로 사용 가능합니다. |
| 27:27 | 변수명: 문자로 시작, 문자·숫자·밑줄, 대소문자 구분, 길이 한도 `namelengthmax`, mnemonic하게. `who`, `whos`, `clear`. |
| 31:46 | Types: double(기본), single, int8–int64, uint8–uint64, char, string, logical. Dynamic typing이지만 타입을 유지하는 습관이 좋습니다. |
| 34:19 | 연산자: + − \* / ^, 음수화. Scientific notation `3e5`. |
| 37:00 | `format short/long/rational`은 표시만 바꿉니다. Ellipsis `...`로 줄을 잇습니다. |
| 41:01 | 우선순위: () → ^ → 음수화 → \* / \\ → + −. 모르면 괄호를 씁니다. |
| 42:56 | `help sin`, `doc sin`. 함수 호출: `abs(-4)`, argument 전달, 값 반환. 연산자도 함수: `plus(2,5)`. |

</details>

<details>
<summary>💡 W1 명령 표 설명</summary>

왼쪽부터 명령, 하는 일, 예와 결과, 함정입니다. 이 주는 환경과 대입이 핵심이고 우선순위 문제가 퀴즈로 나왔습니다(Intro I Q2).

</details>

---
[장 목차](README.md) · [과목 지도](../../README.md) · [M2 Introduction II: 상수, 난수, 타입, 논리, 함수, 파일 →](M2_Introduction-II-상수-난수-타입-논리-함수-파일.md)
