# How to run chrome headless with extensions

### In order to run extension in headless mode, you need to launch browser using [`Xvfb`](/xvfb/how-to-install-xvfb-on-ubuntu-ubuntuversion):

```bash
xvfb-run google-chrome --remote-debugging-port=9222 --disable-gpu  https://www.google.com
```

- `xvfb-run` - [lib:xvfb](/xvfb/how-to-install-xvfb-on-ubuntu-ubuntuversion) framebuffer launcher
- `--remote-debugging-port` - specify port to listen for [debugging protocol](/chrome-headless/chrome-remote-interface-usage-example)


