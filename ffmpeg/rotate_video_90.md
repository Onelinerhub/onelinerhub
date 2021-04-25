# Rotate a video 90 degrees clockwise

Will rotate ```in.mp4``` 90 clockwise, write results to ```out.mp4```. Use ```transpose=2``` to rotate 90 counter clockwise.

```bash
ffmpeg -i in.mp4 -vf "transpose=1" out.mp4
```

- -i in.mp4 - video file that will be rotated
- -vf "transpose=1" - transpose video filter that will rotate video 90 clockwise, use other values:
  - ```transpose=0``` 90 counter cLockwise + vertical flip
  - ```transpose=1``` 90 clockwise
  - ```transpose=2``` 90 counter clockwise
  - ```transpose=3``` 90 clockwise + vertical flip
