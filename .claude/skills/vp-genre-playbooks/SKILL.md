---
name: vp-genre-playbooks
description: 장르·용도별 영상 프롬프트 플레이북. "호러", "공포", "커머스", "제품 리뷰", "광고", "야생동물", "다큐", "뮤직비디오", "MV", "애니", "UGC", "국뽕", "사건", "우주" 등 채널·장르가 정해진 컷을 만들 때 로드. 장르마다 카메라·조명·모션·오디오의 기본값이 다르고, 잘못된 기본값이 화면을 광고컷으로 만든다. 세부 플레이북은 references/ 에 있다. 라우터=video-prompt-router.
user-invocable: true
---

# 장르 플레이북

> 🔴 **착수 전 필독 — [실패 정본 `vp-failure-registry`](../vp-failure-registry/SKILL.md)**
> 이 스킬의 규칙은 전부 **실패로 산 것**이다. 반증된 처방 8건·소환 사고 8건·비용 사고 5건이 거기 있다.
> 엔진·코드 실패는 the engine failure log (not included).


> **핵심 명제**: 장르를 선언하지 않으면 모델이 **기본값**으로 간다.
> 기본값 = **밝은 조명 + 카메라 응시 + 미소 + 중앙 정렬** = 광고컷.
> 다큐·호러·서정 컷이 이상해 보이는 이유의 대부분이 이것이다.

## 1. 장르 판정 → 플레이북

| 채널·상황 | 플레이북 |
|---|---|
| 사건기록부 · 사에키 · 실화 재현 | `references/horror-incident.md` |
| 쇼핑 · 커머스 · 제품 리뷰 · UGC 광고 | `references/commerce-ugc.md` |
| 사바나 · Wildhearted · 동물 | `references/wildlife.md` |
| music-mv · the recurring character MV · 홍보 쇼츠 | `references/music-mv.md` |
| 우주 · 공법 · 지식 다큐 | `references/documentary.md` |
| 애니 · 스타일라이즈드 | `references/anime-stylized.md` |

## 2. 장르 무관 공통 기본값 (전부 명시하라)

| 축 | 안 쓰면 나오는 것 | 대응 |
|---|---|---|
| 시선 | 카메라 응시 | `eyes on the horizon` / `gaze lowered` / `seen from behind` |
| 표정 | 미소 | `mouth relaxed and closed` + 감정의 신체 외화 |
| 조명 | 균일 밝음 | 광원 개수·방향·경도·색온도 4요소 |
| 구도 | 중앙 정렬 | 앵글 + 화면 점유 분수 |
| 카메라 | 미세 드리프트 | `Static camera shot.` 맨 앞 + 오염어 제거 |
| 속도 | 느림 | 속도어 + 동작에 맞는 duration |

## 3. 엔진 `genre` 파라미터 (Seedance / Cinema Studio)

`seedance_2_0`·`seedance_2_0_mini`·`cinematic_studio_3_0`는 `genre` 파라미터를 받는다:
`auto` · `action` · `horror` · `comedy` · `noir` · `drama` · `epic`

⚠️ **파라미터는 프롬프트를 대체하지 않는다.** 힌트일 뿐이고, 조명·카메라를 오버라이드할 수 있어
정적 컷에 `action`을 걸면 카메라가 움직인다. **기본은 `auto`, 확신이 있을 때만 지정.**
Kling·Veo에는 이 파라미터가 없다 → **본문 스타일 어휘로만** 장르를 만든다.

## 4. 🔴 장르가 표현 수위를 정하지 않는다

**표현축(수위)과 소재축(무엇을 다루는가)은 별개다.**
게이트 통과 = 소재가 옳다는 뜻이 아니고, 무거운 소재라고 자기검열할 이유도 없다.
🔴 **검열은 상류에서 들어온다** — 대본이 아니라 기획 문서에 수위 제한 절을 만들면 화면까지 밋밋해진다.
( ·)

## 5. 공통 체크리스트

- [ ] 장르 플레이북을 **읽고** 시작했는가
- [ ] 시선·표정·조명·구도·카메라·속도 **6축을 전부 명시**했는가
- [ ] `genre` 파라미터가 정적 컷의 카메라를 흔들고 있지 않은가
- [ ] 채널의 **기존 룩 락을 상속**했는가
