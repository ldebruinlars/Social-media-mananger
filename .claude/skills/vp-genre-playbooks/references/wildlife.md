# 야생동물 플레이북 (사바나 · Wildhearted)

| 축 | 값 |
|---|---|
| 조명 | `golden hour, low sun raking across the grass, long shadows` / `overcast, flat soft light` |
| 카메라 | 망원 압축 `telephoto compression, shallow depth of field` — 관찰자 시점 |
| 색 | `warm savanna palette, dust haze` / `cold overcast, desaturated` |
| 속도 | 🔴 **슬로모 금지**(the studio lead 극혐) — `real-time pace` + 동작에 맞는 duration |
| 표정 | 🔴 **무표정 동물 금지** — 귀·꼬리·눈·주둥이의 미세 제스처를 명시 |

## 🔴 종(species) 드리프트 — 이 장르 최대 사고
1. **학명을 쓰지 마라.** 모델이 학명을 모른다 → **모델이 아는 템플릿**으로 서술
   (`Aegithalos caudatus` ❌ → `a tiny round long-tailed tit, white head, black eye stripe, fluffy body` ✅)
2. 🔴 **내가 종 이름을 썼으니 맞겠지** 가 함정이다. 이름을 적어도 화면은 다른 종이 된다 → **스틸에서 확정**
3. **뒷모습 스틸 + 고개 돌리기 = 종 드리프트 확정.** 스틸에 없는 정보는 프롬프트로 못 이긴다 → 컷 분리
4. **해부 락은 긍정 카운트**: `exactly four legs, one tail, two ears` (`no extra limbs` ❌)
5. **와이드 컷은 룩 락을 잃는다** — 락은 종만 잠그고 룩은 안 잠근다 → 실루엣·색면으로 재서술

## 오디오
🔴 **생성 오디오 끄기 필수.** Seedance가 **종이 틀린 울음소리**를 얹은 실측 있음.
SFX는 ElevenLabs 등으로 따로 붙인다.

## 프롬프트 골격
```
Static camera shot, telephoto compression, shallow depth of field.
<모델이 아는 종 서술 5요소> <완결동작 1개, 끝상태>. exactly four legs, one tail, two ears,
ears flicking, tail giving one slow sweep. <환경>, golden hour, long shadows, dust haze in the air.
The camera does not move. The only movement is <앰비언트>.
```

## 수치·해부 검증
🔴 널리 퍼진 수치일수록 **①1차출처 ②표본수 ③학명**을 확인하고 써라. 대본의 숫자가 틀리면 컷도 틀린다.
동물 해부 인서트는 `(not in this pack)` 정본 사용 — `gpt-image`는 동물 뇌를 **사람 뇌로 그린다**.

## 퍼널
쇼츠 ↔ 롱폼을 **종 이름으로 매칭**해 배선하라(`_engine/funnel_wire.py`). 같은 소재의 쇼츠 337k / 롱폼 829회 사례 있음.
