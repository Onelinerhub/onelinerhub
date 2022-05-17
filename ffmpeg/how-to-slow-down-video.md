# How to slow down video

```bash
ffmpeg -i in.mp4 -filter:v "setpts=2*PTS" out.mp4
```

- `-i in.mp4` - input video file
- `-filter:v` - apply specified video filter
- `setpts` - filter is used to change video speed 
- `2*PTS` - will slows down video to half of its original speed
- `out.mp4` - resulting video file

group: speed


