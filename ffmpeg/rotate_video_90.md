# Rotate a video 90 degrees clockwise

Will rotate ```in.mp4``` 90 clockwise, write results to ```out.mp4```. Use ```transpose=2``` to rotate 90 counter clockwise.

```bash
ffmpeg -i in.mp4 -vf "transpose=1" out.mp4
```
