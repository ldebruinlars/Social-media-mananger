# 커머스 · 제품 · UGC 광고 플레이북 (쇼핑 채널 · 쿠팡 · 마케팅)

## 이 장르만 기본값이 맞다
광고컷의 기본값(밝음·응시·미소·중앙)이 **여기서는 정답**이다. 다른 장르에서 싸우던 것을 여기선 쓴다.

| 축 | 값 |
|---|---|
| 조명 | `soft key from camera left, large diffused source, gentle fill, clean highlights` |
| 시선 | 제품 → 카메라 순 (`glances down at the product, then up to the lens`) |
| 배경 | 단순·저채도 — 제품이 유일한 채도원 |
| 색 | `clean, neutral grade, slightly warm skin tones` |
| 카메라 | 느린 push-in 1개 또는 고정 |

## 🔴 손↔물체 정밀동작 = 이 장르의 핵심 난제
문 열기·컵 들고 마시기·물건 집기는 **Kling이 손/컵/문을 모핑**시킨다.

**정답 경로**: Seedance 2.0 **std**(reference-driven, 물리 결맞음 우수) — 🔒봉인 시 studio approval 필요
**Kling 대체 처방**:
1. 손을 **물체에 앵커** (`her hand rests on the cup handle`)
2. **완결 동작 1개**만 (`lifts the cup to her lips, then holds`)
3. 동사를 `subtle`/`slow`로 완화
4. `<물체> keeps its solid shape` 병기
5. 그래도 모핑되면 **컷을 분리**(집는 컷 / 마시는 컷)

## 스케일 앵커 (제품 컷 필수)
제품이 미니어처가 되거나 거대해지는 사고가 잦다. **스틸 단계**에서 잡아라:
```
CRITICAL SCALE: the <제품> is <손/얼굴> 대비 <구체 비율>, natural human proportions,
correct real-world perspective, full hand visible holding it.
```

## 프롬프트 골격
```
<제품> <완결동작 1개>, <환경>. Camera holds completely static.
IDENTITY LOCK: same face throughout, natural human proportions, five fingers.
Constraints: hand anchored on <물체>, smooth natural motion, <물체> keeps its solid shape.
Soft key from camera left, large diffused source, clean neutral grade.
```

## 발행 규율
- 브랜드명·로고를 프롬프트에 넣지 마라 → 워터마크 환각
- 표시광고법·식약처 필터를 대본 단계에서 통과시켜라
- Marketing Studio(`marketing_studio_video`)는 별도 경로 — hook_id/setting_id 조합 사용
