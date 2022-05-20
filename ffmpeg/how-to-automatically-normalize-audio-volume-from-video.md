# How to automatically normalize audio volume from video

```bash
ffmpeg-normalize in.mp4  -c:a aac -b:a 192k -o out.mp4
```

- `ffmpeg-normalize` - handly [audio normalization tool](/ffmpeg/how-to-install-ffmpeg-normalize-on-ubuntu-ubuntuversion)
- `in.mp4` - input video file to normalize audio for
- `-o out.mp4` - output video with normalized audio
- `-c:a aac` - use [`AAC`](/ffmpeg/how-to-set-audio-quality-for-aac) codec for output file
- `-b:a 192k` - use 192k bitrate for output audio

group: ffmpeg-normalize


link_youtube: https://youtu.be/I6QnKCKqHsA
