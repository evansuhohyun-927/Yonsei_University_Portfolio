# M5 Matrix tools and linear systems

특수 행렬을 만들고, Ax = b를 inv, backslash, rref 세 방법으로 풉니다. det = 0이면 해의 개수는 rref로 확인합니다. <sub>〔W5〕</sub> <sub>〔37:02〕</sub>

| 명령 | 하는 일 | 예 → 결과 | 함정 |
|---|---|---|---|
| `diag(A)` / `diag(v)` | 대각 추출(열벡터) / 대각행렬 생성 | `trace(A) = sum(diag(A))` | 입력이 행렬이냐 벡터냐로 기능이 바뀝니다. |
| `eye(n)` | 단위행렬 | 3×4 M: `M*eye(4)` = `eye(3)*M` = M | 오른쪽은 열 수, 왼쪽은 행 수 |
| `det(A)` | 행렬식 | `det([1 2; 2 4])` → 0 | 0이면 "유일해 없음"만 알려 줍니다. |
| `inv(A)` | 역행렬 | singular이면 경고와 Inf | 큰 행렬에서는 느립니다. |
| `[A b]` `[A eye(n)]` | 첨가행렬 | `rref([A eye(3)])` | 옆으로 붙일 때 공백·쉼표, 세미콜론은 아래로 |
| `inv(A)*b` | 역행렬로 풀기 | 2×2 Practice 1 | b는 열벡터 |
| `A\b` | backslash 풀이 | `[2 1; 1 -3]\[5; -1]` → \[2; 1\] | 더 빠르고 정확. `b/A`와 방향 반대 |
| `rref([A b])` | RREF로 해의 구조 확인 | `x = ans(:,end)` | singular이면 마지막 행으로 해 없음·무한을 구별 |
| `rref(A,tol)` | pivot tolerance 지정 | singular에 가까운 행렬 | 고급 옵션 |

```matlab
A = [2 1; 1 -3]; b = [5; -1];
det(A)                  % -7, 가역
x1 = inv(A)*b           % [2; 1]
x2 = A\b                % [2; 1]
R = rref([A b]); x3 = R(:,end)
Ai = rref([A eye(2)]); Ai = Ai(:,3:4)   % 역행렬
```

<details>
<summary>📎 세션 시간표</summary>

Week 5 · 5주차 강의 비디오.mp4 / 5주차.mp3 / WEEK 5 - MATLAB SESSION.txt

|   |   |
|---|---|
| 00:51 | MATLAB의 두 도구: 행렬 표현(numeric)과 `solve`(symbolic). 이번 세션은 행렬 표현입니다. |
| 03:18 | Square, diagonal, `randi([1,20],4)`. |
| 05:27 | `diag(A)`는 대각 추출(열벡터), `diag(v)`는 대각행렬 생성. `trace(A)`, `sum(diag(A))`. |
| 08:46 | `eye(n)`. M이 3×4이면 `M*eye(4)`, `eye(3)*M`. |
| 11:09 | `inv(A)`. singular이면 경고와 Inf. det = 0은 "유일해 없음"만 알려 줍니다. |
| 15:15 | Augmented matrix `[A eye(size(A))]`, `[A b]`. |
| 16:59 | 행렬 형태 AX = b, x = A⁻¹b. |
| 18:35 | `inv(A)*b` vs `A\b`: backslash가 빠르고 정확합니다. |
| 21:50 | Practice 1: 2×2 시스템. `det(A)`로 가역 확인(= 2) → `x = inv(A)*b`, b는 열벡터로 입력. |
| 23:23 | 교수님 설명: backslash는 더 일반적이지만 singular일 때 해가 없는지 무한한지 알려 주지 않습니다. 이때 구조는 `rref`로 확인합니다. |
| 24:03 | `rref`: 정확한 답보다 해의 구조를 드러냅니다. `rref([a b])`, `x = ans(:,end)`. |
| 24:42 | `rref`는 답을 끝까지 주지 않고 해를 읽을 수 있는 형태까지 "준비"해 줍니다. |
| 25:56 | `rref(A,tol)`: pivot tolerance 인자. singular에 가까운 행렬에서 쓰는 고급 옵션입니다. |
| 29:41 | 역행렬: `rref([a eye(size(a))])`, `ans(:,4:6)`. |
| 30:24 | 4×4 연습: det, inv, backslash, rref 세 풀이가 일치합니다. |
| 33:30 | det = 0 사례: b = (1,2)면 해 없음, b = (1,−1)이면 해 무한. rref의 마지막 행으로 구별합니다. |

</details>

<details>
<summary>💡 W5 명령 표 설명</summary>

Ax = b를 푸는 세 방법과 행렬 도구입니다. backslash가 기본이고, 해의 개수가 의심되면 rref로 봅니다.

</details>

---
[← M4 Operations: 함수, 집계, 배열 연산, 논리 인덱싱, 행렬곱](M4_Operations-함수-집계-배열-연산-논리-인덱싱-행렬곱.md) · [장 목차](README.md) · [과목 지도](../../README.md) · [M6 9주차 (MATLAB Week 6): LU decomposition과 계산량 →](M6_9주차-MATLAB-Week-6-LU-decomposition과-계산량.md)
