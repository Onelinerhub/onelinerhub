# Extract a specific frame from a video into jpg

This will extract frame at 4 min 50 sec from ```in.mp4``` and save it to ```out.jpg```.

```bash
ffmpeg -accurate_seek -ss 00:04:50 -i in.mp4 -frames:v 1 out.jpg
```
