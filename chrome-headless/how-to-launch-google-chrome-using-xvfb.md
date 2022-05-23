# How to launch Google Chrome using Xvfb

### As opposed to [headless](/chrome-headless/how-to-open-url-in-headless-mode) mode you can launch Chrome in [Xvfb](/xvfb/how-to-install-xvfb-on-ubuntu-ubuntuversion) environment:

```bash
xvfb-run google-chrome
```

- `xvfb-run` - [lib:xvfb](/xvfb/how-to-install-xvfb-on-ubuntu-ubuntuversion) framebuffer launcher
- `google-chrome` - we want to open Google Chrome in background


