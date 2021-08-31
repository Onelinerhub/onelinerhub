# How to play sound in a chrome-extension

Should be executed in [content script](https://developer.chrome.com/docs/extensions/mv3/content_scripts/),
which is [specified in manifest.json](/chrome-extension/content_script).

```
var sound = new Audio(chrome.runtime.getURL('sound.mp3'));
sound.play();
```

- var sound - audio object to play mp3
- chrome.runtime.getURL - get URL for public extension resource (mp3 file in our case)
- sound.mp3 - file we want to play (should be located in extension folder and added to [web_accessible_resources](chrome-extension/web_accessible_resources))
- sound.play() - plays selected file
