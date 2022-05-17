# How to speed up video

```bash
ffmpeg -i in.mp4 -filter:v "setpts=0.5*PTS" out.mp4
```

- `-i in.mp4` - input video file
- `-filter:v` - apply specified video filter
- `setpts` - filter is used to change video speed 
- `0.5*PTS` - will speed up video to double of its original speed
- `out.mp4` - resulting video file

group: speed


