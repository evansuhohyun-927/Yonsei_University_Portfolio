# M7 10주차 (MATLAB Week 7): Matrix Models

이주 모델은 x<sub>k+1</sub> = Mx<sub>k</sub> 반복, Leontief는 (I − C)x = d 한 번 풀기입니다. 아래 M7.1–M7.4가 이론, 위젯, 실습 코드입니다. <sub>〔W10〕</sub> <sub>〔31:37〕</sub>

| 명령 | 하는 일 | 예 → 결과 | 함정 |
|---|---|---|---|
| `%%` | Run Section 단위 | `%% Practice 1` | 스크립트 `Week7_practice.m` |
| `M*x0` | 한 해 진행 | `[0.93 0.05; 0.07 0.95]*[800000; 500000]` | x0는 열벡터 |
| `M^k*x0` | k년 뒤 | `M^10*x0` | `M.^10`은 성분별 |
| `for k = 1:10 … end` | 반복 | `x = M*x;` | `M^10*x0`와 같은 답 |
| `round(x,5)` | 소수 5자리 반올림 | `round(748252/38041430,5)` → 0.01967 |   |
| `sum(C)` | 열 합 | `max(sum(C))` = 0.9293 | 기본이 열 합 |
| `(eye(n)-C)\d` | Leontief 풀이 | x ≈ (225.9, 118.5, 77.8) | 권장 방법 |
| `rats(x)` | 소수를 분수로 표시 | `rats(x)` → 2400/29 … | 표시만 바뀝니다. |
| `eye(size(C))` | C와 같은 크기의 I | `(eye(size(C)) - C) \ d` | eye 크기를 손으로 쓰면 틀리기 쉽습니다. |
| `X(:,k+1) = M*X(:,k)` | 모든 해의 상태 저장 | `X = zeros(2, n+1)` | 인덱스는 1부터: 2015년이 `X(:,1)` |
| `o - C*o` | 객관식 보기 검산 | 결과가 d인 보기가 정답 | Migration은 보기 합이 초기 총인구인지 봅니다. |

```matlab
% 모든 해의 상태를 저장하고 그리기 (W10 Quiz 정리)
n = 10;
X = zeros(2, n+1);        % 각 열 = 그해의 상태 벡터
X(:,1) = x0;
for k = 1:n
    X(:,k+1) = M*X(:,k);
end
sum(X)                    % 매년 총인구가 같은지 확인
plot(2015:2015+n, X', '-o'); legend('City','Suburbs');
```

<details>
<summary>📎 세션 시간표</summary>

10주차 · 10주차 강의 비디오.mp4 / .mp3 / .docx (TurboScribe, 30:00까지) · 슬라이드 표기 "MATLAB Week 7", 28쪽

|   |   |
|---|---|
| 00:00 | 표지 "MATLAB Week 7". 음성은 "week six"라고 말합니다. 이번 주부터 MATLAB 응용입니다. |
| 00:45 | Difference equations: dynamic system을 이산 시간에 측정해 x₀, x₁, x₂, …를 얻고 x<sub>k+1</sub> = Ax<sub>k</sub>로 씁니다. (p.2–3) |
| 03:15 | 인구 이동 모델: 도시와 교외, 2000년 x₀ = (r₀, s₀). |
| 05:15 | 매년 도시 5% → 교외, 교외 3% → 도시. 1년 뒤 분포 식 (4), (5). |
| 06:30 | x₁ = Mx₀ (6), M = \[0.95 0.03; 0.05 0.97\]은 migration matrix입니다. (p.6) |
| 08:30 | 비율이 일정하면 x<sub>k+1</sub> = Mx<sub>k</sub>. (p.7) |
| 09:00 | Leontief input-output model: n개 부문, production vector x, open sector, final demand d. |
| 10:00 | 중간 수요: 생산자도 투입재를 소비합니다. 생산 = 중간 수요 + 최종 수요가 되는 x가 있는가. |
| 11:00 | Unit consumption vector c₁, c₂, c₃ (제조·농업·서비스). |
| 12:15 | Example 1: 제조업 100단위 → 100c₁ = (50, 20, 10). |
| 13:45 | 중간 수요 = x₁c₁ + x₂c₂ + x₃c₃ = Cx (11), C (12). Leontief model x = Cx + d (13). |
| 16:00 | (I − C)x = d (14). Example 2: d = (50, 30, 20). |
| 17:45 | 첨가행렬 row reduction → 226, 119, 78 단위. |
| 18:00 | Theorem: C, d ≥ 0이고 열 합 &lt; 1이면 (I − C)⁻¹ 존재, x = (I − C)⁻¹d (15)는 음수 없는 유일해 (16). |
| 19:30 | 열 합 &lt; 1의 경제적 의미. Example의 열 합은 0.8, 0.8, 0.6. (p.17) |
| 21:00 | 실습 안내: `Week7_practice.m`, `%%` 섹션과 Run Section. 필요한 도구 `*`, `^`, `for`, `eye`, `sum`, `A\b`, `inv(A)*b`, `rref([A b])`. (p.18–19) |
| 21:45 | Practice 1: 7%/5%, 2015년 800,000 / 500,000 → 2017년. |
| 23:00 | Practice 1 풀이: x₁ = (769,000, 531,000), x₂ = (741,720, 558,280), `sum(x2)` = 1,300,000. |
| 24:30 | Practice 2: California 38,041,430명, 그 밖 275,872,610명, 유출 748,252명, 유입 493,641명. (p.21) |
| 25:00 | Practice 2 풀이: `round(…, 5)`로 비율 0.01967, 0.00179, `for k = 1:10` 또는 `M^10`. 2022년 California ≈ 35,728,987명. (p.22) |
| 26:45 | Leontief in MATLAB: backslash, `inv`, `rref` 세 방법 → (225.9, 118.5, 77.8). A\\b 권장. (p.23) |
| 28:15 | Practice 3: C = \[0.2 0.2 0; 0.3 0.1 0.3; 0.1 0 0.2\], d = (40, 60, 80). |
| 28:45 | Practice 3 풀이: x = (2400, 3800, 3200)/29 ≈ (82.8, 131.0, 110.3). 차원이 크면 backslash가 사실상 유일한 방법이라고 설명합니다. |
| 29:15 | Practice 4: 1958년 미국 경제, 81부문 → 7부문. (p.27) |
| 30:45 | Practice 4 풀이: 최대 열 합 0.9293 &lt; 1, x ≈ (99,576, 97,703, 51,231, 131,570, 49,488, 329,554, 13,835) 백만 달러. 30:00 이후는 transcript가 없어 프레임 OCR로 확인했습니다. (p.28) |
| 31:00 | 마무리: practice를 homework로 낸다는 안내. 음성이 불명확해 문항 수는 과제 공지로 확인합니다(W10 Models의 Whisper 전사). |

</details>

현실 문제를 행렬 × 벡터 식 하나로 바꾸고 계산은 MATLAB에 맡깁니다. 시간이 흐르는 문제는 x<sub>k+1</sub> = Ax<sub>k</sub>를 반복하고, 균형을 찾는 문제는 (I − C)x = d를 풉니다. <sub>〔W10 00:00–31:37〕</sub>

폴더에 이 주차 슬라이드 PDF는 없습니다. 내용은 transcript(30:00까지)와 15초 간격 영상 프레임 OCR(127장)로 확인했습니다. 교재 대응은 Lay, *Linear Algebra and Its Applications* §1.10, §2.6입니다. Practice 1은 Lay §1.10 Exercise 9, Practice 4는 §2.6 Exercise 13과 같은 수치로 보입니다(추정). `보완` <sub>〔W10 Atlas〕</sub>

---
[← M6 9주차 (MATLAB Week 6): LU decomposition과 계산량](M6_9주차-MATLAB-Week-6-LU-decomposition과-계산량.md) · [장 목차](README.md) · [과목 지도](../../README.md) · [M7.1 Linear difference equation →](M7.1_Linear-difference-equation.md)
