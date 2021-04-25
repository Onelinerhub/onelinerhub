# Rotate a video 90 degrees clockwise

```bash
ffmpeg -i in.mp4 -vf "transpose=1" out.mp4
```

- -i in.mp4 - video file that will be rotated
- -vf - apply specific video filters
- transpose=1 - transpose video filter that will rotate video 90 clockwise, use other values:
  : transpose=0 : 90 counter cLockwise + vertical flip
  : transpose=1 : 90 clockwise
  : transpose=2 : 90 counter clockwise
  : transpose=3 : 90 clockwise + vertical flip
- out.mp4 - resulting file
