# How to crop video based on coordinates

```bash
ffmpeg -i in.mp4 -vf "crop=300:200:20:50" out.mp4
```

- `-i in.mp4` - input video file
- `-vf` - apply specific video filters
- `crop=` - crop video
- `300:200` - crop size (`300` height and `200` height)
- `20:50` - X (`20`) and Y (`50`) coordinates to crop from
- `out.mp4` - resulting video file

group: zoom


