# jjambabBot

[![Python version](https://img.shields.io/badge/python-3.5%2C%203.6%2C%203.7-blue.svg)](https://python.org)
[![Discord](https://discordapp.com/api/guilds/129489631539494912/widget.png?style=shield)](https://discord.gg/hvN6Ndn)

짬밥봇은 [discord.py](https://github.com/Rapptz/discord.py)라이브러리를 사용하여 만들었습니다. 군 복무기간중 연습삼아 처음 만든 디스코드봇 이며 공부를 목적으로 제작 하였기에 완성도, 최적화 면에서는 많이 부족합니다. 기능은 특정 시간이 되면 구글 스프레드 시트의 내용을 읽어와 불러주는 식으로 


![Main](https://i.imgur.com/FWcHtcS.png)

### Setup
Setting up the MusicBot is relatively painless - just follow one of the [guides](https://just-some-bots.github.io/MusicBot/). After that, configure the bot to ensure its connection to Discord.

The main configuration file is `config/options.ini`, but it is not included by default. Simply make a copy of `example_options.ini` and rename it to `options.ini`. See `example_options.ini` for more information about configurations.

### Commands

There are many commands that can be used with the bot. Most notably, the `play <url>` command (preceded by your command prefix) will download, process, and play a song from YouTube or a similar site. A full list of commands is available [here](https://just-some-bots.github.io/MusicBot/using/commands/ "Commands").

### Further reading

* [Support Discord server](https://discord.gg/bots)
* [Project license](LICENSE)
