# How to play sound

```
var sound = new Audio(chrome.runtime.getURL('sound.mp3'));
sound.play();
```

- `var sound` - audio object to play mp3
- `chrome.runtime.getURL` - get URL for public extension resource (mp3 file in our case)
- `sound.mp3` - file we want to play (should be located in extension folder and added to [web_accessible_resources](/chrome-extension/web_accessible_resources))
- `sound.play()` - plays selected file


link_youtube: https://youtu.be/cbp6V_GNNW0
