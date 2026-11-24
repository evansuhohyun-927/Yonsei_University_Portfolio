# 주차별 정리 (1–13주차)

1–13주차의 이론(Ch1–Ch7, 슬라이드 387쪽)과 MATLAB 세션 7회 + Week 8 Review를 주차별로 나눠 정리했어요. 각 주차는 **이론**과 **MATLAB 세션**을 따로 두었어요.

| 항목 | 내용 |
|---|---|
| 과목 | SED2103-01 Linear Algebra, Fall 2026 (UIC) |
| 분량 | 슬라이드 Ch1 25 · Ch2 33 · Ch3-1 46 · Ch3-2 66 · Ch4 32 · Ch6 40 + 50 · Ch7 64 + 31쪽 |
| MATLAB | M1–M5(1–5주차), M6 LU(9주차), M7 Matrix models(10주차), Week 8 Review(11주차) |
| 평가 자료 | HW1–HW6-2, MATLAB 퀴즈 W1–W8, 중간고사(10/21–23, 25문항) |

| 주차 | 이론 | MATLAB 세션 | 과제·퀴즈 |
|---|---|---|---|
| 1–2 | Ch1 벡터, Ch2 연립방정식 | M1 Intro I, M2 Intro II | HW1, HW2, Intro I·II 퀴즈 |
| 3–4 | Ch3-1 행렬 연산·역행렬 | M3 Vectors·Matrices, M4 Operations | HW3-1, Week 4 퀴즈 |
| 5 | Ch3-2 subspace·독립·해의 기하 | M5 Matrix tools·linear systems | Week 5 퀴즈 |
| 6–7 | Ch3-2 special forms·LU·partitioned | 없음 | HW3-2 |
| 8 | 중간고사 | — | Midterm 25문항 |
| 9 | Ch4 행렬식·고유값 | M6 LU decomposition·계산량 | HW4, W6 Review Quiz |
| 10 | Ch6-1 선형변환·standard matrix | M7 Matrix models (이주, Leontief) | HW6-1, W7 Homework |
| 11 | Ch6-2 kernel·range·합성·wireframe | Week 8 Review (그래픽스·필터) | HW6-2, W8 Review |
| 12–13 | Ch7 차원·구조, 정사영·QR | 없음 | (Ch7 과제 아직 없음) |

이론 주차 배정은 과제 마감일과 슬라이드 순서로 **추정**했어요. MATLAB 주차는 세션 파일 기준이에요.

핵심 3줄

- 앞 절반(1–8주차)은 **Ax = b를 푸는 법**(row reduction, 역행렬, LU)과 해의 구조(**subspace, independence**)예요.
- 뒤 절반(9–13주차)은 행렬을 **변환**으로 보고(det, eigenvalue, linear transformation) 공간의 **구조**(rank–nullity, 네 fundamental space, projection, QR)를 다뤄요.
- MATLAB은 같은 내용을 계산으로 확인해요: `A\b`, `rref`, `lu`, `M^k*x0`, `(eye(n)-C)\d`, homogeneous 좌표 행렬.

## 주차 노트

- [ ] [1–2주차 — 벡터와 연립방정식](01-02주차_벡터와-연립방정식.md)
- [ ] [3–4주차 — 행렬 연산과 역행렬](03-04주차_행렬-연산과-역행렬.md)
- [ ] [5주차 — Subspace와 해의 기하](05주차_Subspace와-해의-기하.md)
- [ ] [6–7주차 — 특수 행렬, LU, 분할 행렬](06-07주차_특수-행렬-LU-분할-행렬.md)
- [ ] [8주차 — 중간고사 (10/21–23)](08주차_중간고사.md)
- [ ] [9주차 — 행렬식과 고유값](09주차_행렬식과-고유값.md)
- [ ] [10주차 — 선형변환과 matrix models](10주차_선형변환과-matrix-models.md)
- [ ] [11주차 — Kernel·range, 합성, 그래픽스](11주차_Kernel-range-합성-그래픽스.md)
- [ ] [12–13주차 — 차원·구조, 정사영·QR](12-13주차_차원-구조-정사영-QR.md)

## MATLAB 코드 모음

세션 순서대로 시험에 다시 쓸 만한 코드만 모았어요. 주석은 결과예요.

```matlab
%% M3-M4 (3-4주차) 인덱싱과 배열 연산
mat = [1:3; 44 9 2; 5:-1:3];   % [1 2 3; 44 9 2; 5 4 3]
mat(3,2)                       % 4
mat(:,4) = [8; 11; 33];        % 4열 추가
reshape(mat, 2, 6)             % 열 순서 유지
v = [7 2 9 4 10]; v(v > 5)     % [7 9 10]
max(max(mat))                  % 전체 최댓값

%% M5 (5주차) Ax = b 세 가지 풀이
A = [2 1; 1 -3]; b = [5; -1];
x1 = inv(A)*b                  % [2; 1]
x2 = A\b                       % [2; 1], 권장
R  = rref([A b]); x3 = R(:,end)

%% M6 (9주차) LU, PA = LU
A = [2 6 2; -3 -8 0; 4 9 2]; b = [2; 2; 3];
[L, U, P] = lu(A);
y = L\(P*b);  x = U\y          % [2; -1; 2]

%% M7 (10주차) 이주 모델과 Leontief
M = [0.93 0.05; 0.07 0.95]; x0 = [800000; 500000];
M^2*x0                         % [741720; 558280]

%% M8 (11주차) moving average 필터
y = [9 5 7 3 2 4 6 5 7 6 8 10 9 5 7];
z = (y(1:end-2) + y(2:end-1) + y(3:end))/3   % 7 5 4 3 4 5 6 6 7 8 9 8 7

%% Ch7 (12-13주차) 확인용
A = [1 3 5; 1 1 0; 1 1 2; 1 3 3]; b = [-2; 3; -1; 2];
[Q, R] = qr(A, 0);  xhat = R\(Q'*b)   % [0.5; 2.5; -2]
rank(A), null(A, 'r')
```

---
[과목 지도](../../README.md)
