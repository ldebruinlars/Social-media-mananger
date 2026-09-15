---
name: vp-director-techniques
description: 실제 영화 감독들의 명명된 카메라 연출 기법을 i2v로 재현하는 스킬. "감독처럼", "영화처럼", "돌리줌", "버티고", "랙포커스", "스노리캠", "1점투시", "더치앵글", "갓즈아이", "오너", "히치콕", "큐브릭", "핀처", "에드가 라이트" 키워드 또는 시네마틱 연출을 흉내 낼 때 로드. 🔴 기법은 이름이 아니라 기구(mechanism)로 써야 모델이 실행한다. 라우터=video-prompt-router.
user-invocable: true
---

# 감독 기법 재현

> 🔴 **착수 전 필독 — [실패 정본 `vp-failure-registry`](../vp-failure-registry/SKILL.md)**
> 이 스킬의 규칙은 전부 **실패로 산 것**이다. 반증된 처방 8건·소환 사고 8건·비용 사고 5건이 거기 있다.
> 엔진·코드 실패는 the engine failure log (not included).

> **핵심 명제**: 모델은 **`Vertigo effect`·`Kubrick shot`을 모른다.**
> 기법은 **이름이 아니라 기구(어떤 장비가 어떻게 움직여 화면이 어떻게 변하는가)** 로 써야 실행된다.
> `cinematic` 이 정보가 0인 것과 같은 이유다(`vp-camera-grammar` §3).

## 1. 🔴 이름 → 기구 변환 (이 스킬의 핵심)

| 기법(이름) | ❌ 이렇게 쓰면 안 됨 | ✅ 기구로 풀어쓰기 |
|---|---|---|
| **돌리줌 / 버티고** | `vertigo effect`, `dolly zoom` 단독 | `the camera pulls backwards while the lens zooms in at exactly the same rate, so she stays the same size in frame while the walls stretch away behind her` |
| **랙포커스** | `rack focus` | `the blurred railing in the near foreground snaps into sharp focus while she goes soft behind it, then the focus pulls back to her` |
| **스노리캠** | `snorricam` | `the camera is rigged to her body: she stays locked in the centre of the frame at a constant size while the walls and sky swing around her` |
| **1점 투시(큐브릭)** | `Kubrick shot` | `symmetrical one-point perspective, the corridor receding to a single central vanishing point, the horizon dead level, the camera moving along the exact centre line` |
| **더치앵글** | `dutch angle` | `the camera arcs around her` ← 🔴 **우리 실측에서 롤이 안정적으로 나온다** |
| **크래시 줌(에드가 라이트)** | `crash zoom` | `the lens rushes in on her fast until her shoulders fill the frame, then stops` ✅검증 |
| **휩팬(PTA)** | `whip pan` | `the camera snaps hard to the right as she passes the pillar, the frame smearing, then catches her again and holds` ✅검증 |
| **갓즈아이** | `god's eye view` | `directly overhead, looking straight down at her from above, her shadow moving beside her` |
| **트렁크샷(타란티노)** | `trunk shot` | `low framing from inside a box looking up at two faces leaning over the opening` |
| **히어로 로우앵글** | `hero shot` | `from ground level just behind her heels, the wet asphalt filling the bottom of the frame, she towers above the lens` |

## 2. 🔴 무엇을 시도할 수 있고 무엇을 못 하는가

우리 법칙(`vp-camera-grammar` §2-B)이 그대로 적용된다 — **피사체의 새로운 면을 요구하면 실패**한다.

### 실측 결과 (2026-07-30 · `veo3_1_lite` 6초, 동일 시작 스틸)

| 기법 | 결과 | 화면에서 확인한 것 |
|---|---|---|
| **돌리줌 (Vertigo)** | ✅✅ | 바닥·벽이 **방사형으로 늘어나며 원근 왜곡**, 인물 크기는 유지 |
| **랙포커스** | ✅✅ | 난간이 선명해지며 **인물이 흐려졌다가**, 다시 인물로 초점 복귀 |
| **갓즈아이** | 🔶 **부분** | 순간전환은 안 되고 **크레인으로 올라가 위에서 내려다보는 시점에 도달** |
| **스노리캠** | ❌ | 평범한 추적샷 — 세계가 인물 주위로 흔들리지 않음 |

### 🔴🔴 여기서 법칙이 한 번 더 정밀해졌다

> **인접 시점은 "이동해서" 도달할 수 있다. 반대편은 못 간다.**

| | 예 | 판정 |
|---|---|---|
| **인접 시점**(위·뒤·안쪽) — 스틸에 부분적으로 보이는 면 | 크레인 상승, **갓즈아이**, 푸시인 | ✅ 이동하면 도달 |
| **반대편**(옆·앞·주체의 시야) — 스틸에 전혀 없는 면 | **오빗**, **POV**, **스노리캠** | ❌ 불가 |

- 갓즈아이는 **머리·어깨 윗면**이 스틸에 이미 부분적으로 보여서 외삽이 가능했다
- 스노리캠은 **인물의 정면**을 프레임에 고정해야 하는데 그 면이 없다 → 실패
- 🔴 **순간 전환을 요구하지 마라.** `directly overhead` 를 원해도 모델은 **거기까지 이동**한다.
  진짜 톱다운이 첫 프레임부터 필요하면 **스틸을 톱다운으로 만들어라**

### 🔴🔴 엔진 대조 — **갈리는 건 "렌즈" 축뿐이다** (동일 스틸·동일 프롬프트 · 대각선까지 실측)

| 기법 | 축 | Kling 3.0 | Veo 3.1 Lite | 판정 |
|---|---|---|---|---|
| **랙포커스** | 렌즈 | 🔶 약함 — 이동이 안 보임 | ✅✅ **n=2 재현 성공** | 🔴 **Veo 전용** |
| **돌리줌** | 렌즈 | ❌ **화면이 소용돌이로 붕괴** | ✅✅ **피사체가 크면 2/2 성공**(작으면 0/3) | 🔴 **Veo + 큰 피사체** |
| **1점 투시 후퇴** | 위치 | ✅ | ✅ | 둘 다 |
| **갓즈아이** | 위치 | 🔶 크레인으로 도달 | 🔶 크레인으로 도달 | 둘 다(부분) |
| 고정·크래시줌·휩팬·크레인·추적·조트 | 위치 | ✅ (Gen7) | (미실시) | Kling 검증됨 |
| **스노리캠** | 시점 | (미실시) | ❌ | 불가 |

🔴 **정밀화된 라우팅 규칙**
> **위치가 변하는 기법(돌리·팬·크레인·줌·1점투시·갓즈아이) → 두 엔진 모두 된다**
> **렌즈가 변하는 기법(랙포커스·돌리줌) → `veo3_1_lite` 만**

"Veo가 감독기법에 강하다"가 아니다 — **갈리는 축은 정확히 "렌즈"뿐**이다.
- Kling은 `warps`·`expands` 같은 **기하 변형 어휘를 문자 그대로 받아** 화면을 붕괴시킨다

### 🔴🔴 정정 — **돌리줌은 확률적이 아니다. 변수는 "피사체 크기"였다** (Gen18 · n=5)

~~"돌리줌은 확률적이다"~~ 는 **틀린 결론이었다.** 스틸의 피사체 크기로 깔끔하게 갈린다:

| 스틸의 피사체 크기 | 결과 | 실측 |
|---|---|---|
| ❌ **프레임의 ~2%**(복도 끝의 작은 인물) | **0/3 실패** — 그냥 강한 푸시인, **인물이 소실** | zoom +58.5 / +64.1 / +115.7% |
| ✅ **프레임 높이의 ~1/3** | **2/2 성공** — 인물 크기가 유지되고 **벽만 늘어난다** | local **76.8 / 82.6** (최상위) |

```
스틸에 반드시: her head and torso occupying roughly the central third of the frame height,
              the corridor walls receding symmetrically past her on both sides
```
🔴 **왜**: 돌리줌은 "피사체 크기 유지 + 배경 왜곡"이다. 유지할 피사체가 작으면 **유지할 대상이 없어** 푸시인으로 붕괴한다.
우리 규칙 **"피사체 크기를 면적 분수로 명시"**가 여기서도 지배한다.

⚠️🔴 **계측기로 돌리줌을 판정하지 마라.** `motion_metric` 의 `zoom`은 전역 아핀 스케일이라
**배경이 확대되면 큰 값이 나온다**(성공 팔도 +70%). **"피사체 크기가 유지되는가"를 눈으로** 봐야 한다.
- ✅ **랙포커스는 n=2 재현** — 신뢰하고 써도 된다
- 💡 Veo lite가 **더 싸다**(1.0 vs Kling pro 1.75 cr/초)
- ⚠️ 단 Veo는 **인물 다컷 불가**(레퍼런스 없음) — 광학 기법 컷 **한 컷만** 보내라

## 3. 기법의 감정적 목적 (무엇을 쓸지 고르는 기준)

기법은 장식이 아니라 **감정 도구**다. 목적에서 역산해 고르라.

| 원하는 감정 | 기법 | 왜 |
|---|---|---|
| 내면으로 들어감·집중 | **느린 푸시인** | 관객과 인물의 거리를 좁힌다. 느릴수록 자연스럽고, 빠를수록 충격적 |
| 거리감·고립·전모 공개 | **풀아웃 / 크레인 이탈** | 맥락을 드러내며 인물을 작게 만든다 |
| 영웅적·위협적 | **로우앵글** | 인물이 렌즈 위에 선다 |
| 나약함·압도됨 | **하이앵글 / 갓즈아이** | 인물을 환경에 눌리게 한다 |
| 심리적 불안 | **더치앵글** | 수직선이 기울어 머리를 갸웃한 느낌 |
| 발밑이 꺼지는 감각 | **돌리줌** | 피사체는 그대로인데 세계만 늘어난다 |
| 몰입·동행 | **트래킹** | 관객을 장면 안으로 끌고 들어간다 |
| 주의 이동·발견 | **랙포커스** | 카메라를 안 움직이고 시선만 옮긴다 |
| 긴박·리듬 | **휩팬 + 크래시줌** | 에드가 라이트식 속도감 |

🔴 **모티베이션 원칙(디킨스)**: *"모든 카메라 이동에는 이야기상의 이유가 있어야 한다."*
이유 없는 무브는 **생명력만 깎는다**(우리 실측: 카메라 문구가 앰비언트를 −11~23%).
→ **목적이 없으면 카메라를 움직이지 마라. 그 예산을 앰비언트에 써라.**

## 4. 프레이밍 기법 (무브 없이 쓰는 것)

| 기법 | 기구 |
|---|---|
| **자연 프레임**(디킨스) | `framed through the doorway, the door edge dark on both sides of frame` |
| **대칭 1점 투시**(큐브릭) | `symmetrical, the corridor receding to a single central vanishing point` |
| **네거티브 스페이스** | `she sits in the lower right, the rest of the frame empty wall` |
| **오버더숄더** | `over his shoulder, his shoulder dark in the near left third` |
| **실루엣** | `she reads as a single dark shape against the lit window` |

## 5. 조합 규칙

- 🔴 **기법도 샷당 하나** — 원-무브 규칙은 감독 기법에도 적용된다
- **돌리줌은 예외적으로 복합**(돌리+줌 동시)이지만, 그것 자체가 하나의 기구다. 다른 무브를 얹지 마라
- 프레이밍 기법(§4)은 무브와 **함께 써도 된다** — 서로 다른 축이기 때문
- 배속·컷 리듬은 **후반**에서 만든다(에드가 라이트식 속도감의 절반은 편집이다)

## 6. 체크리스트

- [ ] 기법을 **이름이 아니라 기구**로 썼는가
- [ ] 그 기법이 **피사체의 새로운 면을 요구하지 않는가**(요구하면 스틸부터)
- [ ] 이 무브에 **이야기상의 이유**가 있는가 (없으면 빼고 앰비언트로)
- [ ] 샷당 기법이 **하나**인가
- [ ] 결과를 **필름스트립으로 확인**했는가
