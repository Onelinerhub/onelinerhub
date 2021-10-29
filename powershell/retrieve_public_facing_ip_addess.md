# How to retrieve your internet's public facing IP address in powershell

```Powershell
(Invoke-WebRequest -Uri "http://checkip.dyndns.com").Content -replace "[a-z]|[A-Z]","" -replace "(<>)|(</>)|(:)",""
```
- (Invoke-WebRequest -Uri "http://checkip.dyndns.com") - send an HTTP GET request  for domain url checkip.dyndns.com to retrieve data
- .Content -replace "[a-z]|[A-Z]","" -replace "(<>)|(</>)|(:)","" - clean the data from the content property on the web response and replace all html style tags besides the IP number