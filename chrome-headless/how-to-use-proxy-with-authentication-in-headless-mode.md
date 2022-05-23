# How to use proxy with authentication in headless mode

### The simplest way is to use additional [proxycnahins](/proxychains/how-to-install-proxychains-on-ubuntu-ubuntuversion) utility to implement proxy authentication for Google Chrome headless mode. Mind configuring [`/etc/proxychains.conf`](/proxychains/how-to-configure-proxychains) file before usage:

```js
proxychains google-chrome --headless --screenshot="screen.png" "https://onelinerhub.com"
```

- `--headless` - will launch chrome in [headless mode](https://developers.google.com/web/updates/2017/04/headless-chrome#cli)
- `--screenshot` - make screenshot and save it to specified file
- `proxychains` - utility from [lib:proxychains](/proxychains/how-to-install-proxychains-on-ubuntu-ubuntuversion) package to add proxy functionality to programs

## Example: 
```js
cat /etc/proxychains.conf
```
```
[ProxyList]
socks5	1.2.3.4	123	user	pwd
```

