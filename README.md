# jjambabBot

[![Python version](https://img.shields.io/badge/python-3.7%2C%20-blue.svg)](https://python.org)
[![Discord](Discord server)](https://discord.gg/hvN6Ndn)

짬밥봇은 [discord.py](https://github.com/Rapptz/discord.py)라이브러리를 사용하여 만들었습니다. 군 복무기간중 연습삼아 처음 만든 디스코드봇 이며 공부를 목적으로 제작 하였기에 완성도, 최적화 면에서는 많이 부족합니다. 기능은 특정 시간이 되면 구글 스프레드 시트의 내용(짬밥)을 읽어와 불러주는 식으로 구성 되있습니다.

### 설정
서버는 [Heroku](https://heroku.com)를 이용하기에 설정파일인 `Procfile`(worker: 실행할 파일), `requirements.txt`(다운 받을 api들), `runtume.txt`(python-3.7.6)등이 있습니다.

### 명령어

메시지 앞에 "/"를 붙여 사용합니다.(ex./오늘 짬밥)
/? 사용가능한 모든 명령어를 출력해줍니다.

### 기타

* [Discord server](https://discord.gg/hvN6Ndn)
* [Project license](LICENSE)
