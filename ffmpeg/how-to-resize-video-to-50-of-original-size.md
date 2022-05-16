# How to resize video to 50% of original size

```bash
ffmpeg -i in.mp4 -vf 'scale=-1:ih/2' out.mp4
```

- `-i in.mp4` - input video file
- `-vf` - apply specific video filters
- `scale=` - scale video
- `-1` - width will be automatically calculated based on aspect ratio
- `ih/2` - height is calculated as half of input height `ih` 
- `out.mp4` - resulting video file

group: resize


