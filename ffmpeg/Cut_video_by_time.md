# Cut video based on start/end time

Will cut ```in.mp4``` from 10 secs to 1 min 30 secs, write result to ```out.mp4```.

```bash
ffmpeg -i in.mp4 -ss 00:00:10 -t 00:01:30 -async 1 out.mp4
```
