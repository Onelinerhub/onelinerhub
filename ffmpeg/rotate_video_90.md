# Rotate a video 90 degrees clockwise

```bash
ffmpeg -i in.mp4 -vf "transpose=1" out.mp4
```

- `-i in.mp4` - video file that will be rotated
- `-vf` - apply specific video filters
- `transpose=1` - transpose video filter that will rotate video 90 clockwise, use other values:
- `out.mp4` - resulting file


link_youtube: https://youtu.be/oBoM6G-Mkqw
