# How to download a playlist as audio using CLI from Youtube

```bash
youtube-dl --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 160K --output "C%(playlist_index)s.%(ext)s" --yes-playlist PLA8M-jgOlTEfMXltdGK3fxIxKqPYJXDii
```

- `youtube-dl` - CLI [lib:python-based script](https://github.com/ytdl-org/youtube-dl/blob/master/README.md#readme) to download Youtube videos
- `--extract-audio` - we ask youtube-dl to download only audio
- `PLA8M-jgOlTEfMXltdGK3fxIxKqPYJXDii` - playlist ID to download
- `--output` - output files name format

group: audio


