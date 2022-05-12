# Convert video to a series of images

```bash
ffmpeg -i in.mp4 -vf fps=1/5 img%04d.jpg
```

- `-i in.mp4` - input video file
- `-vf fps=1/5` - create one image every 5 seconds of video
- `img%04d.jpg` - output image name template (will look like "img0001.jpg, img0002.jpg...")

group: images


link_youtube: https://youtu.be/wJiJZcukGo0
