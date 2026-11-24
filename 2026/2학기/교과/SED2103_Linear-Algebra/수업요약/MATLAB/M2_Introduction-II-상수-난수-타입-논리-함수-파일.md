# M2 Introduction II: 상수, 난수, 타입, 논리, 함수, 파일

타입과 범위를 알고, 난수를 원하는 구간으로 바꾸고, 내장 수학 함수의 규칙(라디안, 밑 e)을 지킵니다. <sub>〔W2〕</sub> <sub>〔37:53〕</sub>

| 명령 | 하는 일 | 예 → 결과 | 함정 |
|---|---|---|---|
| `pi` `i` `j` `inf` `NaN` | 내장 상수 | `1/0` → Inf, `0/0` → NaN | e는 상수가 없어 `exp(1)` |
| `rand` | (0,1) 균등 실수 | `a + (b-a)*rand` → (a,b) | `rand(3)`은 3×3 행렬 |
| `randn` | 표준정규 (평균 0, 표준편차 1) | `randn(1,5)` | 범위가 −1–1로 제한되지 않습니다. |
| `randi` | 균등 정수, 양 끝 포함 | `randi([5,10])`, `randi(10)` → 1–10 | `randi(10)`은 0을 포함하지 않습니다. |
| `rng` | seed 설정 | `rng('shuffle')`, `rng(1)` | 같은 seed면 같은 난수열 |
| `int8`…`uint64` | 정수 타입 변환 | `int8(200)` → 127 | 범위를 넘으면 saturate, 소수는 반올림 |
| `intmin` `intmax` | 타입의 범위 | `intmax('int8')` → 127 |   |
| `class` `cast` | 타입 확인 / 변환 | `class(3)` → double | 기본 숫자 타입은 double |
| `'...'` `"..."` | char vector / string | `double('a')` → 97, `char('a'+2)` → c | 공백도 문자 |
| `== ~= > <` | 관계 연산, 결과 logical 1/0 | `3 > 2` → 1 | `=`(대입)과 `==`(비교) 혼동 |
| `&& \|\| ~ xor` | 논리 연산 | `xor(true,true)` → 0 | 우선순위: not → 관계 → and → or |
| `sin` / `sind` | 라디안 / 도 | `sind(30)` → 0.5 | `sin(pi)`는 0이 아니라 1.2246e−16 |
| `fix floor ceil round` | 0 쪽 / 아래 / 위 / 가까운 쪽 | `fix(-2.7)` → −2, `floor(-2.7)` → −3 | 음수에서 fix와 floor가 다릅니다. |
| `rem` `mod` | 나머지 | `rem(-7,3)` → −1, `mod(-7,3)` → 2 | 음수에서 부호가 다릅니다. |
| `log log10 log2 exp` | 자연로그 / 상용 / 밑 2 / e^x | `log(100)` → 4.6052 | log는 밑 e |
| `save` `load` | MAT-file 저장·불러오기 | `save data x`, `save data y -append` | M-file은 코드, MAT-file은 변수 |

```matlab
r = 10*rand            % (0,10) 실수
k = randi([5,10])      % 5–10 정수
z = int8(200)          % 127 (saturate)
c = char('a'+2)        % 'c'
t = xor(true,true)     % 0
[fix(-2.7) floor(-2.7) ceil(-2.7) round(-2.7)]   % -2 -3 -2 -3
save data x            % 변수 x만 data.mat에
```

<details>
<summary>📎 세션 시간표</summary>

Week 2 · 2주차 강의 비디오.mp4 / 2주차.mp3 / WEEK 2 - MATLAB SESSION.txt

|   |   |
|---|---|
| 00:40 | 상수: `pi`, `i`, `j`, `inf`, `NaN`. 결측 데이터도 NaN으로 읽힙니다. |
| 02:48 | Pseudo-random, seed. `rng('shuffle')`로 시계 기반 seed 설정. |
| 05:44 | `rand`: (0,1) 균등. `rand(n)` n×n. 범위 변환: `10*rand`, `2*(rand-0.5)`. |
| 09:31 | `randn`: 정규분포. `randi([m,n])`: 양 끝 포함 정수. |
| 13:14 | `randi(10)`은 1–10 정수, 범위를 `randi([0,10])`처럼 주면 양 끝 포함. `rand`는 소수점 있는 실수, `randi`는 균등 정수입니다. |
| 14:35 | Character: 작은따옴표 char vector, 큰따옴표 string. 공백도 문자입니다. |
| 16:31 | 관계연산자 > &lt; >= &lt;= == ~=. 결과는 logical 1/0. 논리연산자 \|\| && ~, `xor`. Truth table과 교환법칙. |
| 20:32 | 확장 우선순위: 괄호, 거듭제곱, not, 곱나눗, 합차, 관계, and, or. 불확실하면 괄호. |
| 21:01 | 정수 범위 `intmin`, `intmax`. Casting `int32(num)`, `class`, `cast`. MATLAB은 dynamic allocation. |
| 25:31 | `double('a')` = 97, `char(97)`. 인코딩 65535 문자, 앞 128자는 ASCII. |
| 26:18 | 삼각함수: `sin`(라디안), `sind`(도), `asin`, `sinh`. `sin(pi)`는 0에 가까운 작은 수. |
| 28:28 | `fix`, `floor`, `ceil`, `round`, `rem`, `mod`, `sign`, `sqrt`, `nthroot`, `deg2rad`, `rad2deg`. |
| 31:36 | `log`(밑 e), `log10`, `log2`, `exp`. 상수 e는 없으므로 `exp(1)`을 씁니다. |
| 33:08 | M-file: New Script에 코드 저장, 이름으로 실행 (`test`). MAT-file: 변수 저장. `save file`, `save file x`, `save -append`, `load file`. |
| 37:08 | MATLAB Online, 모바일, 클라우드, 툴박스. |

</details>

<details>
<summary>💡 W2 명령 표 설명</summary>

타입 변환(int8 saturate), 반올림 함수의 음수 처리, 라디안·도, 자연로그가 퀴즈의 함정입니다. 결과 열을 가리고 먼저 예측해 보세요.

</details>

---
[← M1 Introduction I: 환경, 변수, 연산](M1_Introduction-I-환경-변수-연산.md) · [장 목차](README.md) · [과목 지도](../../README.md) · [M3 Vectors and Matrices: 만들기, 인덱싱, 모양 바꾸기 →](M3_Vectors-and-Matrices-만들기-인덱싱-모양-바꾸기.md)
