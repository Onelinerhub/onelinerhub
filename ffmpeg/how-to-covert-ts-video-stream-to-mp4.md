# How to covert TS video stream to MP4

### You can either [download full video stream from an `m3u8` file](/ffmpeg/how-to-download-m3u8-steam-and-save-to-mp4) or convert it directly if it's been downloaded:

```bash
ffmpeg -i in.ts -c:v libx264 -c:a aac out.mp4
```

- `-i in.ts` - input video file
- `-c:v libx264` - use H.264 codec
- `-c:a aac` - use [`AAC` codec](/ffmpeg/encode-mp3-to-aac) for audio
- `out.mp4` - resulting video file


link_youtube: https://youtu.be/L4yAialogm0
