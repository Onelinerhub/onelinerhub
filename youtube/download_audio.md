# How to download audio using CLI from youtube

This will download the video file and convert to audio

```bash
youtube-dl --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 160K https://youtu.be/lxiI8G0IDY4
```

- youtube-dl - CLI [python-based script](https://github.com/ytdl-org/youtube-dl/blob/master/README.md#readme) to download Youtube videos
- https://youtu.be/lxiI8G0IDY4 - URL of the video file you want to convert to audio
