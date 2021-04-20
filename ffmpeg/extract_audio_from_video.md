# Extract audio from video

Will extract audio from ```in.mp4``` and writes it to ```out.mp3```.

```bash
ffmpeg -i in.mp4 -vn -q:a 0 -map a out.mp3
```
