# 호러 · 사건 재현 플레이북 (사건기록부 · 사에키 · 실화 재현)

## 기본값 뒤집기
| 축 | 이 장르의 값 |
|---|---|
| 조명 | **단일 광원 + 큰 미광부.** `a single bare bulb overhead, hard-edged shadows, deep falloff into darkness` |
| 시선 | 카메라 응시 **금지** — `gaze fixed on something off-frame left` |
| 표정 | 미소 금지 — `mouth closed, jaw tight, eyes unblinking` |
| 카메라 | 핸드헬드 미세 흔들림 또는 완전 고정. **중간이 없다** |
| 색 | `desaturated, crushed shadows, sickly green cast` / `cold blue with sodium orange practicals` |
| 속도 | 액션 컷은 **배속 1.5~1.6** 전제로 발주(달리기 1.6 · 근접 격투 1.5) |

## 프롬프트 골격
```
Static camera shot. <피사체> <완결동작 1개, 끝상태 포함>.
<장소>, a single <광원> from <방향>, hard-edged shadows, deep falloff into darkness.
Desaturated, crushed shadows, cold blue with sodium orange practicals. Film grain, dust in the air.
The camera does not move. The only movement is <앰비언트 1개>.
```

## 이 장르의 함정
- 🔴 **죽음·의식불명은 '있는 상태'로 서술**하라. `dead`/`lifeless`는 부재라서 모델이 살아 움직이게 만든다
  → `lying motionless, limbs slack, eyes closed, chest still`
- 🔴 아동·의식불명 이미지는 moderation에 걸린다 → `unconscious` → **`sleeping`** 으로 치환
- 🔴 **실제 사건 영상은 실제 아카이브**를 써라. 재현 컷으로 대체하면 신뢰가 깨진다
- 🔴 **가정법이 하류에서 사실이 된다** — "만약 ~였다면"이 요약 단계에서 조건절을 잃고 재현 컷까지 제작된다.
  대본의 조건절은 **컷 지시로 내려보내지 마라**
- 몬스터·비명 SFX = ElevenLabs SFX (모델 생성 오디오 금지 — 종·톤이 틀린다)
- 아카이브 검색어가 **책 표지**를 물어오는 오염 주의(유명 사건일수록)

## 훅 (첫 3~5초)
공감 + 이득을 던지고 **결론부터**. 화면엔 궁금증 제목 띠를 끝까지, 소리는 결론선행.
영상은 **띠 아래**에 배치.
