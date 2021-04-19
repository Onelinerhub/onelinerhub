# Select specific video/audio track when converting video

Will convert ```input.mkv``` to ```output.mp4```. Will select first (index of 0) video track (0:v```:0```) and second (index of 1) audio track (0:a```:1```).

```bash
ffmpeg -i input.mkv -map 0:v:0 -map 0:a:1 output.mp4
```
