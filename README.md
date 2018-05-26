# qwqaq-webhook-server
A light-weight web server for reacting GitHub Webhooks and executing shell commands.

一个简单 WEB 服务器，当接收到 GitHub Webhooks 后执行命令，如 `git pull`，仅此而已

## Requirements
- Python 3
- Flask

## Quick Start

首先，配置 `qwqaq-webhook-server.py` 中的 `HOOK_ACTIONS=[]`，然后：

```sh
python qwqaq-webhook-server.py
```

> 另：Windows Server 可使用 [NSSM](http://nssm.cc) 让其变成服务，后台运行

## Author
[ZNEIAT](http://www.qwqaq.com)
