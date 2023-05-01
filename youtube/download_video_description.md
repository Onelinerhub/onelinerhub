# How to download the video description with the video

```bash
youtube-dl --write-description https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

- `youtube-dl` - CLI [lib:python-based script](https://github.com/ytdl-org/youtube-dl/blob/master/README.md#readme) to download Youtube videos
- `/watch?v=dQw4w9WgXcQ` - URL of the video you want to download
- `--write-description` - Save the description to a file with the same name as the video file, but with a .description extension. 