# 11주차 — Kernel·range, 합성, 그래픽스

> **이번 주 개념 노트** [6.3 Kernel and range](../Ch6_Linear-Transformations/6.3_Kernel-and-range.md) · [6.4 Composition and invertibility](../Ch6_Linear-Transformations/6.4_Composition-and-invertibility.md) · [6.5 Computer graphics](../Ch6_Linear-Transformations/6.5_Computer-graphics.md)  
> **MATLAB 노트** [M8](../MATLAB/M8_Computer-Graphics-and-Signals.md)

## 이론: Ch6-2 §6.3–6.5 (p. 1–50)

Kernel은 0으로 가는 벡터(= null(A)), range는 나올 수 있는 모든 값(= col(A))이에요. 합성은 **나중에 적용한 변환이 왼쪽**에 와요.

```math
\ker T = \{x : Ax = 0\}, \qquad \mathrm{ran}\,T = \mathrm{col}(A), \qquad [T_2 \circ T_1] = [T_2][T_1]
```

| 개념 | 핵심 |
|---|---|
| One-to-one | ker T = {0} ⇔ 열이 independent |
| Onto | ran T = Rm ⇔ 모든 b에 consistent |
| 정방 A | one-to-one ⇔ onto ⇔ det ≠ 0 (unifying theorem) |
| Inverse operator | \[T⁻¹\] = \[T\]⁻¹ |
| Wireframe (§6.5) | vertex matrix V의 열 = 꼭짓점, connectivity matrix는 대칭·대각 0. 상의 vertex matrix = AV |
| Homogeneous 좌표 | (x, y, 1)로 옮겨서 평행이동도 행렬곱으로 만들어요 |

## MATLAB 세션: Week 8 Review problems (MATLAB Week 8)

그래픽스 변환은 homogeneous 좌표의 3×3(또는 4×4) 행렬을 **순서대로 왼쪽에** 곱해요. 신호 필터는 moving average 행렬을 데이터에 곱하는 것과 같아요.

```math
z_k = \frac{y_{k-1} + y_k + y_{k+1}}{3}, \qquad M = T \cdot R, \quad T = \begin{bmatrix} 1 & 0 & h \\ 0 & 1 & k \\ 0 & 0 & 1 \end{bmatrix}
```

> [!NOTE]
> Week 8 Review 문항의 답은 공개 리포라 뺐어요. 강의 내용과 Exercise 1–3은 [M8 노트](../MATLAB/M8_Computer-Graphics-and-Signals.md)에 있어요.

---
[← 10주차](10주차_선형변환과-matrix-models.md) · [주차별 목차](README.md) · [과목 지도](../../README.md) · [12-13주차 →](12-13주차_차원-구조-정사영-QR.md)
