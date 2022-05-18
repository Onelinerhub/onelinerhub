# Scaling video with zscale filter example

```bash
ffmpeg -i in.mp4 -vf zscale=w=-1:h=180 out.mp4
```

- `-i in.mp4` - input video file
- `-vf` - apply specific video filters
- `zscale=` - apply [zscale filter](https://ffmpeg.org/ffmpeg-filters.html#zscale-1)
- `w=-1` - calculate width automatically based on aspect ratio
- `h=180` - set height to `180` pixels
- `out.mp4` - resulting video file


