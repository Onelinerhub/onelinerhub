# Set jpeg quality when extracting from video

```bash
ffmpeg -i input.mp4 -q:v 2 output_%03d.jpg
```

- `-i input.mp4` - name of the video to convert
- `-q:v 2` - image of the best quality possible (`2...31` for good to worst quality)
- `output_%03d.jpeg` - files to write extracted images to

group: convert_video

