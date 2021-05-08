# Convert video to h264

```bash
ffmpeg -i input.mp4 -c:v libx264 -preset ultrafast -crf 17 output.mkv
```

- -i input.mp4 - input video to convert
- -c:v libx264 - select video codec, h264 lib in this case
- -preset ultrafast - encode faster but produce larger file (use ```-preset veryslow``` for better compression)
- -crf 17 - sets quality to the very good one (use ```-crf 0``` for lossless encoding)
- output.mkv - resulting h264 video file

group: convert_video
