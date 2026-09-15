# 뮤직비디오 플레이북 (music-mv · the recurring character MV · 홍보 쇼츠)

> 상세 연출 정본 = `(not in this pack)` · 립싱크 정본 = `(not in this pack)`. 여기는 **프롬프트 문법**만.

## 3축 레퍼런스 락 (MV의 생명)
```
① FACE   ② WARDROBE   ③ SET
```
빠뜨린 축은 컷마다 모델 마음대로 간다. 세 축을 **모든 컷에 동일 문장으로** 복사하라.

| 축 | 값 |
|---|---|
| 조명 | 곡 톤에 종속. 우울곡 = `dim, single practical source, deep falloff` · 밝은곡 = `soft wrapped light` |
| 표정 | 🔴 슬픈 곡 = **미소 금지** `mouth relaxed and closed, eyes lowered` · 우울곡 = **덤덤·속삭임** |
| 카메라 | 컷당 1무브. the recurring character 고정 + 세계 회전(오빗) 패턴 유효 |
| 색 | 곡별 그레이드 문장 1개를 정해 **전 컷 공유** |

## 립싱크 (컷 단위 예외)
- 🔴 **Seedance 2.0 std + 1080p 고정** — 모션 tier 무관. Kling엔 **오디오 입력 슬롯 자체가 없다**
- 립싱크 컷은 얼굴이 정적이라 휴리스틱이 `low_motion`으로 **오분류** → 대본에 `motion_tier` 명시
- **입은 하나** — 오버레이 합성 금지(잔상)
- 간주·와이드·실루엣·입다문 컷은 **예외 아님** → Kling. 원가 절감의 유일한 수단 = **립싱크 컷 수 줄이기**
- 어두운 곡은 **검은 화면 립싱크**가 유효

## 컷 길이 · 편집
- 🔴 **15초를 다 쓰지 마라** — 컷 길이를 변주하라
- 🔴 **클립 < 슬롯이면 슬로모가 강제**된다 → 발주 길이를 슬롯 이상으로
- 🔴 **죽은 구간 = 4.6~8.5초** — 5초 컷이 10초 발주가 되어 절반을 버린다. 발주 단위에 맞춰 컷을 설계하라

## 쇼츠(홍보) 파생
- 🔴 **기존 MV의 룩 락을 상속**하라 — 새로 만들지 마라
- 잔잔한 곡의 쇼츠 훅 = **첫 1초 시각 공감**
- 자막은 **whisper 음성인식이 아니라 진짜 가사** · 싱크는 Gemini 줄별 타임스탬프

## 프롬프트 골격
```
<카메라 1무브>. <the recurring character 서술>, <완결동작 1개, 끝상태>.
IDENTITY LOCK: same face throughout — <특징3>; <의상> unchanged; <세트> unchanged;
eyes lowered, mouth relaxed and closed.
<세트>, <광원 4요소>. <곡 전용 그레이드 문장>, film grain, fabric creases.
The only movement is <앰비언트 1개>.
```
