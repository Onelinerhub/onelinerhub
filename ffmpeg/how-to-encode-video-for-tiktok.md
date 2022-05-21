# How to encode video for TikTok

```bash
ffmpeg -i in.mp4 -vf "crop=ih*(9/16):ih" -crf 21 -c:a copy out.mp4
```

- `-i in.mp4` - input video file
- `-vf` - apply specific video filters
- `crop=` - using crop filter to prepare video size for TikTok
- `ih*(9/16):ih` - crop video to become vertical (9x16)
- `-crf 21` - use good quality for encoding
- `-c:a copy` - copy audio without converting
- `out.mp4` - resulting video file

group: exporting


link_youtube: https://youtu.be/RjFYdy9EY90
