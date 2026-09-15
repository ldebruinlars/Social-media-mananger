---
name: vp-lighting-and-look
description: 영상 프롬프트의 조명·색·질감·룩 문법 전용 스킬. "조명", "빛", "색감", "톤", "그레이딩", "필름", "그레인", "황금시간", "역광", "어둡게", "분위기", "무드", "질감" 키워드 또는 컷의 룩을 정할 때 로드. 조명 어휘·색 그레이딩 표기·필름스톡·시간대·질감 어휘와 채널별 룩 상속 규칙 포함. 라우터=video-prompt-router.
user-invocable: true
---

# 조명·색·룩 문법

> 🔴 **착수 전 필독 — [실패 정본 `vp-failure-registry`](../vp-failure-registry/SKILL.md)**
> 이 스킬의 규칙은 전부 **실패로 산 것**이다. 반증된 처방 8건·소환 사고 8건·비용 사고 5건이 거기 있다.
> 엔진·코드 실패는 the engine failure log (not included).


> **핵심 명제**: 조명은 "분위기"가 아니라 **광원의 개수·방향·성질**이다.
> `moody lighting`은 정보가 0이고, `a single practical lamp from camera left, hard shadows`는 정보다.

## 1. 조명 서술 4요소 (전부 있어야 재현된다)

```
[광원 종류] + [방향] + [경도(hard/soft)] + [색온도]
```
예: `a single sodium streetlamp from camera right, hard-edged shadows, warm amber against cool blue night`

| 요소 | 어휘 |
|---|---|
| **광원** | practical lamp · candle · neon sign · monitor glow · firelight · overcast sky · fluorescent overhead · god rays · volumetric fog light |
| **방향** | key light from camera left · backlit / rim light · top-down · underlit · side light · frontal |
| **경도** | hard-edged shadows · soft diffused · wrapped soft light |
| **색온도** | warm amber(2700K) · neutral · cool blue · teal-and-amber · sodium orange · sickly green |

## 2. 시간대 사전 (한 단어로 룩 전체가 결정된다)

| 시간대 | 프롬프트 | 효과 |
|---|---|---|
| 골든아워 | `golden hour, low sun raking across` | 따뜻·긴 그림자·역광 |
| 블루아워 | `blue hour, deep teal sky, lit windows` | 서정·차분 |
| 한낮 | `harsh midday sun, short hard shadows` | 다큐·건조 |
| 흐림 | `overcast, flat soft light, no visible shadows` | 중립·질감 강조 |
| 야간 실내 | `dim interior, single practical light source` | 친밀·긴장 |
| 야간 실외 | `night, wet asphalt reflecting neon` | 🔴 **AI 최고의 친구** |

🔴 **젖은 표면 = AI 비디오 최고의 친구.** 반사·파티클·색대비가 모션 데이터를 풍부하게 만든다.
잔잔한 컷이 밋밋할 때 첫 처방은 **비·안개·젖은 바닥**이다.

## 3. 색 그레이딩 표기

```
desaturated teal-and-amber grade
high-contrast bleach bypass
warm sepia, lifted blacks
cold desaturated, crushed shadows
pastel low-contrast
```
- **grade / graded** 라는 단어를 쓰면 모델이 후반 색보정으로 인식해 전체에 균일하게 적용한다
- 채도 방향(`desaturated` / `saturated`)과 대비 방향(`high-contrast` / `low-contrast`)을 **둘 다** 명시

## 4. 필름스톡·질감

| 목적 | 어휘 |
|---|---|
| 실사감 | `35mm film, fine grain` · `16mm, visible grain` · `shot on 1980s color film, slightly grainy` |
| 디지털 매끈 | `clean digital, no grain` |
| 질감 살리기 | `film grain, skin pores, fabric creases, dust in the air` |
| 렌즈 성질 | `slight lens flare` · `anamorphic streak` · `vignette` · `chromatic aberration at edges` |

🔴 **과매끈 플라스틱 질감의 해독제 = 질감 명사 3개.** `film grain, skin pores, fabric creases`를 붙여라.

## 5. 앰비언트 사전 (잔잔·몽환 컷의 핵심)

정적 컷에서 "살아 있음"을 만드는 것은 인물이 아니라 **환경 미세운동**이다.

`fog drift` · `water ripples` · `rain streaks with neon reflections` · `dust particles in light beams` ·
`candle flicker` · `cloth or hair in gentle wind` · `steam rising` · `subtle camera shake`

공식 패턴:
> `Camera holds completely static. The only movement is gentle fog drift and subtle water ripples.`

⚠️ **모델은 캐릭터·카메라를 환경 이벤트보다 우선한다.**
환경 변화가 주인공인 컷은 **인물 없이 단독 발주**하라 — 인물이 있으면 환경이 죽는다.

## 6. 스타일 어휘 (Seedance 공식 목록 포함)

`Japanese comics` · `American comics` · `line drawing` · `voxel` · `paper-cutting` · `felt` ·
`Chinese ink painting` · `watercolor` · `Chinese animation`
+ 일반: `cinematic` 단독 금지 → `neo-noir` · `documentary handheld` · `Wes Anderson symmetry` · `retro 80s` · `cyberpunk neon`

⚠️ **감독·작가 이름을 스타일로 쓰는 것은 신중히.** 룩은 따라오지만 **상업 발행 시 리스크**가 있다.
가능하면 그 룩을 **구성 요소로 분해**해 서술하라(대칭 구도 + 파스텔 팔레트 + 정면 프레이밍).

## 7. 🔴 룩 상속 규칙 (채널 일관성)

- **같은 영상 내 모든 컷은 같은 그레이드 문장을 공유**해야 한다. 컷마다 다르게 쓰면 편집에서 색이 튄다.
- **쇼츠는 기존 MV/본편의 룩 락을 상속**한다 — 새로 만들지 말고 원본의 조명·그레이드 문장을 그대로 복사.
- 슬픈 곡·무거운 소재는 **어두운 톤 + 미소 금지**를 명시(모델 기본값이 밝고 웃는 얼굴이다).

## 8. 체크리스트

- [ ] 광원의 **개수·방향·경도·색온도**를 전부 썼는가
- [ ] `moody`, `beautiful lighting` 같은 **모호어를 제거**했는가
- [ ] 그레이드에 **채도 방향 + 대비 방향**이 둘 다 있는가
- [ ] 질감 명사(그레인·모공·주름)를 넣었는가
- [ ] 정적 컷이면 **앰비언트 요소**가 최소 1개 있는가
- [ ] 환경이 주인공인 컷에 **인물이 섞여 있지 않은가**
- [ ] 같은 영상의 다른 컷과 **그레이드 문장이 동일한가**
