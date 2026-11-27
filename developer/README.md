# Play 개발자 프로필

Play 콘솔 › 개발자 계정 › Play 개발자 프로필에 넣는 자료다. 개발자 ID 7769092577978646068, 표시 이름 ghbcode.

| 칸 | 값 |
|---|---|
| 헤더 이미지 | [`header.png`](header.png) — 4096×2304, 24비트 PNG(투명 없음), 1MB 이하 |
| 추천 앱 | 스티커 메이커(`kr.ghbcode.stickermaker`) — 프로덕션 공개 앱만 고른다. 터치패드·삐삐는 비공개 테스트라 넣지 않는다 |
| 개발자 웹사이트 | https://ghbcompany.github.io/ |
| 광고 문구(필수, 140자) | 기본 언어 en-US: `Small, focused apps that do just what you need.` · 번역 ko-KR: `꼭 필요한 기능만 담은 작은 앱을 만듭니다.` |

기본 언어가 영어(en-US)라 광고 문구는 영어 칸이 반드시 차 있어야 저장된다(2026-11-27 한국어만 넣었을 때 «일부 언어에 오류가 있습니다»로 저장 거부).

헤더는 세 앱의 스토어 아이콘(`docs/play/icon-512.png`)과 나눔스퀘어라운드 글꼴로 `make_header.py` 가 그린다. 생성형 AI 는 쓰지 않는다.
기기마다 가장자리가 잘려 보일 수 있어 글자와 아이콘을 가운데에 모았다. 앱이 늘거나 아이콘이 바뀌면 다시 만든다.

```bash
python3 make_header.py <sticker-maker 아이콘> <touchpad 아이콘> <beepbeep 아이콘> \
  /usr/share/fonts/truetype/nanum/NanumSquareRoundB.ttf /usr/share/fonts/truetype/nanum/NanumSquareRoundR.ttf header.png
```

내려받기: https://raw.githubusercontent.com/ghbcompany/ghbcompany.github.io/main/developer/header.png
