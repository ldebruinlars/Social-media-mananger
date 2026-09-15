# 애니 · 스타일라이즈드 플레이북

## 스타일 어휘 (Seedance 공식 목록 + 일반)
`Japanese comics` · `American comics` · `line drawing` · `voxel` · `paper-cutting` · `felt` ·
`Chinese ink painting` · `watercolor` · `Chinese animation`
+ `cel-shaded anime, clean linework, flat color fills, limited animation`
+ `2D hand-drawn, visible paper texture`

## 실사 문법을 그대로 쓰면 안 되는 것
| 실사에선 | 애니에선 |
|---|---|
| `shallow depth of field` | 대체로 무의미 — `background painted with soft gradients` |
| `film grain, skin pores` | 🚫 실사화됨 → `flat color fills, clean linework` |
| `35mm film` | 🚫 실사화 + **화면 텍스트 유출 위험** |
| 광원 4요소 | 유효하지만 **`hard cel shadow edges`** 로 경도 지정 |

## 애니 특유 지시
- **한정 애니메이션**: `limited animation, held frames with occasional motion` — 프레임을 다 채우지 말라는 지시
- **효과선·속도선**: `speed lines radiating from the subject`
- **아이캐치**: 수미프레임으로 처리
- 🔴 **타임랩스형 애니 배경**은 검증된 프롬프트 패턴이 따로 있다(달 반세트 등) — 새로 쓰지 말고 재사용

## 프롬프트 골격
```
<카메라 1무브>. Cel-shaded anime, clean linework, flat color fills, hard cel shadow edges.
<피사체> <완결동작 1개, 끝상태>. <배경, soft painted gradients>.
<색 팔레트 2~3색>. Limited animation, held frames with occasional motion.
```

## 주의
- 실사 인물 레퍼런스를 애니 스타일 프롬프트에 넣으면 **어중간한 3D**가 된다 → 스틸부터 애니로
- 스타일 일관성은 **팔레트 문장**이 잡는다 — 컷마다 동일 문장 복사
