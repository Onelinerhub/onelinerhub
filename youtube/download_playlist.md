# How to download a playlist as audio using CLI from youtube

```bash
youtube-dl --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 160K --output "C%(playlist_index)s.%(ext)s" --yes-playlist PLA8M-jgOlTEfMXltdGK3fxIxKqPYJXDii
```

- youtube-dl - CLI [python-based script](https://github.com/ytdl-org/youtube-dl/blob/master/README.md#readme) to download Youtube videos
- PLA8M-jgOlTEfMXltdGK3fxIxKqPYJXDii is the youtube playlist to download

