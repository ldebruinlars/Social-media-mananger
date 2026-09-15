---
name: vp-composition-blocking
description: 구도·배치 문법 — 화면 점유 분수, 전경/중경/배경 층, 리드룸, 대칭·삼분할, 피사체 배치. "구도", "배치", "프레이밍", "화면 어디에", "너무 작게 나온다", "가운데만 있다", "깊이가 없다", "밋밋한 구도" 키워드 또는 컷의 화면 구성을 정할 때 로드. 크기는 샷 이름이 아니라 면적 분수로 말해야 한다. 라우터=video-prompt-router.
user-invocable: true
---

# 구도·배치 문법

> 🔴 **착수 전 필독 — [실패 정본 `vp-failure-registry`](../vp-failure-registry/SKILL.md)**
> 이 스킬의 규칙은 전부 **실패로 산 것**이다. 반증된 처방 8건·소환 사고 8건·비용 사고 5건이 거기 있다.
> 엔진·코드 실패는 the engine failure log (not included).


> **핵심 명제**: 샷 사이즈 이름(`close-up`, `wide`)은 **모델에게 크기를 알려주지 않는다.**
> 크기는 **화면 면적 분수**로, 배치는 **층(layer)** 으로 말해야 한다.

## 1. 🔴 크기는 면적 분수로

```
❌ a close-up of the wolf
✅ the wolf FILLS THE LOWER TWO-THIRDS of the frame
```
어휘: `fills the frame` · `fills the lower two-thirds` · `occupies the left third` ·
`takes up roughly a quarter of the frame` · `small in the lower right, dwarfed by the wall behind`

## 2. 3층 구조 — 깊이는 층에서 나온다

밋밋한 구도의 원인은 대부분 **층이 하나**여서다.
```
전경(foreground) : 프레임 가장자리를 무는 요소 — 흐릿해도 좋다
중경(midground)  : 피사체
배경(background) : 거리감을 주는 요소
```
서술 예:
> `a blurred railing crossing the lower edge in the foreground; the woman in the midground filling
> the central third; the harbour lights far behind, thrown out of focus.`

**전경 요소 사전**: `blurred railing` · `out-of-focus leaves` · `a doorframe edge` ·
`steam crossing the lens` · `a shoulder in the near corner` · `rain on the glass between us and her`

🔴 **전경 하나만 넣어도 깊이가 생긴다.** 가장 싼 품질 레버 중 하나.

## 3. 배치 문법

| 목적 | 서술 |
|---|---|
| 삼분할 | `positioned on the right third, looking into the empty left space` |
| 리드룸(시선 여백) | `space left in front of the direction she faces` |
| 대칭 | `centred and symmetrical, the frame split evenly` |
| 불안 | `pushed to the very edge of the frame, cramped` |
| 고립 | `alone in the centre of a vast empty field, tiny` |
| 압박 | `the ceiling low in frame, pressing down on her` |

## 4. 🔴 스케일 앵커 — 스틸 단계에서만 고칠 수 있다

인물이 배경 사물보다 커지는 사고(문이 미니어처가 됨)는 **i2v로 못 고친다.**
스틸 프롬프트에 넣을 공식:
```
CRITICAL SCALE: the <물체> is clearly TALLER and WIDER than her, the top of the <물체>
is well ABOVE her head, her full body from head to feet is visible standing on the ground,
natural human proportions, correct real-world perspective.
```
+ **medium-wide 전신 프레이밍** (클로즈업이면 스케일 판정 자체가 불가)

## 5. 세로(9:16) 구도 — 쇼츠 전용 규칙

- 🔴 **영상은 제목 띠 아래에** 배치한다 — 상단은 궁금증 띠가 끝까지 차지한다
- 피사체를 **하단 2/3**에 두면 띠와 안 겹친다
- 가로 구도를 세로에 그대로 옮기지 마라 — **수직 요소**(기둥·인물 전신·창틀)를 찾아라
- 얼굴은 **상단 1/3 경계 근처**가 안정 (너무 위면 띠에 먹힘)

## 6. 가로(16:9) 구도 — 미드폼·롱폼

- 좌우 여백을 **층으로 채워라** — 비면 모델이 기본값으로 채운다
- 인서트·그래픽이 들어갈 자리를 **미리 비워 설계**하라(다큐 인서트는 16:9 전용)

## 7. 구도가 무너지는 3가지

| 증상 | 원인 | 대응 |
|---|---|---|
| 피사체가 너무 작다/크다 | 샷 이름만 씀 | 면적 분수로 재서술 |
| 깊이가 없다 | 층이 1개 | **전경 요소 1개** 추가 |
| 배경 사물이 미니어처 | 스틸 구도 | 스틸 단계 스케일 앵커(§4) |
| 와이드에서 룩이 달라짐 | 피사체가 작아져 세부 재발명 | 실루엣·색면으로 재서술 |
| 세로인데 답답 | 가로 구도 이식 | 수직 요소 탐색 |

## 8. 체크리스트

- [ ] 피사체 크기를 **면적 분수**로 썼는가
- [ ] **층이 2개 이상**인가 (전경 요소가 있는가)
- [ ] 시선 방향에 **리드룸**이 있는가
- [ ] 스케일이 중요한 컷이면 **스틸 단계**에서 앵커했는가
- [ ] 9:16이면 피사체가 **하단 2/3**에 있는가
- [ ] 빈 공간을 **의도적으로** 비웠는가 (방치가 아닌가)
