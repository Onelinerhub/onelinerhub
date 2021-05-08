# Convert MOV video to MP4

```bash
ffmpeg -i input.mov -q:v 0 output.mp4
```

- -i input.mov - input video file
- -q:v 0 - this options sets the best possible quality
- output.mp4 - resulting video file

group: convert_video
