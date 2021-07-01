# Launch Google Chrome with proxy server.

```bash
google-chrome --proxy-server=="host:port" --proxy-bypass-list="*.google.com;*.github.com"
```

- google-chrome - google chrome executable ([see here how to launch for your OS](/google-chrome/launch_cli_linux))
- --proxy-server - specify proxy to use browser-wide
- host:port - proxy address and port
- --proxy-bypass-list - list domains (wildcard supported) to bypass specified proxy
