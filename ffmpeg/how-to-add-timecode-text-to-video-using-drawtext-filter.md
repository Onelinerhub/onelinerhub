# How to add timecode text to video using drawtext filter

```bash
ffmpeg -i in.mp4 -vf "drawtext=timecode='00\:00\:00\:00':r=30:x=10:y=10:fontsize=24:fontcolor=white" -c:a copy out.mp4
```

- `-i in.mp4` - input video file
- `-vf` - apply specific video filters
- `drawtext=` - drawtext filter options
- `x=10` - horizontal position in pixels from top left corner
- `y=10` - vertical position in pixels from top left corner
- `fontsize` - size of the text to display
- `fontcolor` - color of the text
- `-c:a copy` - copy audio without converting
- `out.mp4` - resulting video file
- `timecode=` - time code template to use
- `r=30` - set input video frame rate (used to calculate time codes), `30` fps in our case

group: drawtext


