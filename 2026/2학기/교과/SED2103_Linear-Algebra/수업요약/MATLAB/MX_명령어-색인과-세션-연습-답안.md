# MX 명령어 색인과 세션 연습 답안

| 분류 | 명령 | 세션 |
|---|---|---|
| 환경 | `pwd ls cd clc clear who whos help doc format namelengthmax` | W1 |
| 변수·타입 | `ans class cast double single int8…int64 uint8…uint64 char string logical intmin intmax` | W1, W2 |
| 상수 | `pi i j inf NaN` | W2 |
| 난수 | `rand randn randi rng` | W2, W3 |
| 논리 | `== ~= > < >= <= && \|\| ~ xor all any isequal find` | W2, W4 |
| 수학 | `abs sign sqrt nthroot exp log log2 log10 sin cos tan sind cosd asin sinh deg2rad rad2deg fix floor ceil round rem mod` | W1, W2 |
| 파일 | `save load (M-file, MAT-file)` | W2 |
| 생성 | `[ ] : linspace logspace zeros ones eye diag reshape repmat fliplr flipud` | W3, W5 |
| 크기 | `length size numel` | W3 |
| 집계 | `min max sum prod diff` | W4 |
| 연산 | `+ − * / \ ^ .* ./ .^ ' dot cross trace det inv` | W4, W5 |
| 선형계 | `A\b rref [A b] lu` | W5, W9 |
| W10 응용 | `M^k for…end eye(n) sum(C) (I-C)\d inv(I-C)*d rref([I-C d]) round(x,5) %% Run Section` | W10 |
| 보완(자료 외) | `norm acosd null eig polyfit` | 이 자료에서 추가 |

```matlab
% Practice 2.2 (W3 29:40)
mat = [1:3; 44 9 2; 5:-1:3]   % [1 2 3; 44 9 2; 5 4 3]
mat(3,2)                      % 4
mat(2,:)                      % [44 9 2]
size(mat)                     % [3 3]
mat(:,4) = [8;11;33]          % 4열 추가
numel(mat)                    % 12
v = mat(3,:)                  % [5 4 3 33]
v(v(2))                       % v(4) = 33
v(1) = []                     % [4 3 33]
reshape(mat,2,6)              % 2×6, 열 순서 유지

% Practice 2.3 (W4 19:38)
vec - 3;   mat / 3;   mat .^ 2;

% Practice 2.4 (W4 28:33)
vec(find(vec >= 0))
vec(vec >= 0)

% 전체 최댓값 (W4 10:54), 모두 10인 행렬 (W4 12:55)
max(max(mat));   ones(3)*10;
```

| 증상 | 원인 | 해결 |
|---|---|---|
| Incorrect dimensions for matrix multiplication | `*`에서 안쪽 크기 불일치, 또는 행·열벡터 혼동 | `size` 확인, `'`로 전치, 성분별이면 `.*` |
| Arrays have incompatible sizes | `.*` `./`에서 크기 불일치 | 같은 크기로 맞춤 |
| Index exceeds the number of array elements | 범위 밖 읽기 | `numel` 확인 (대입은 확장되지만 읽기는 오류) |
| Unsupported use of the '=' operator | 주석 달린 여러 줄 행렬을 Command Window에 붙여 넣음, 보이지 않는 공백 문자 | 주석 없이 한 줄로 입력하거나 Script로 저장 후 Run (F5) |
| Unrecognized function or variable 'M' | 앞 줄이 실패해 M이 만들어지지 않음 | M부터 다시 정의. 대입은 `=`, 비교는 `==` |
| Matrix is singular to working precision | det = 0인 A에 `inv` 또는 `\` | `rref([A b])`로 해 없음·무한 구별 |
| 값이 비정상적으로 큼 | `M.^10`과 `M^10` 혼동 | 행렬 거듭제곱은 `^` |
| int 연산이 이상함 | `int8` saturate·반올림 | `class`로 타입 확인 |

자주 나는 오류 정리. 오류 문구는 MATLAB 표준 메시지입니다. `보완`

---
[← M8 MATLAB Week 8](M8_Computer-Graphics-and-Signals.md) · [장 목차](README.md) · [과목 지도](../../README.md)
