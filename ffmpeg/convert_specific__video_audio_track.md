# Select specific video/audio track when converting video

Will convert ```input.mkv``` to ```output.mp4```. Will select #0 video track (0:v:```0```) and #1 audio track (0:a:```1```).

```bash
ffmpeg -i input.mkv -c:v libx264 -c:a ac3 -crf 20 -map 0:v:0 -map 0:a:1 output.mp4
```
