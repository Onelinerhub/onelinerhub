# Create video from a series of images

```bash
ffmpeg -r 1/5 -i img%04d.jpg -c:v libx264 -vf fps=25 -pix_fmt yuv420p out.mp4

```

- `ffmpeg` - basic ffmpeg utility
- `-r 1/5` - show each image for 5 serconds
- `-i img%04d.jpg` - input images names template (e.g. `img0001.jpg, img0002.jpg,...`)
- `-c:v libx264` - use h264 coded
- `-vf fps=25` - set framerate to 25
- `-pix_fmt yuv420p` - use `yuv420p` as pixel format
- `out.mp4` - resulting file

group: images


link_youtube: https://youtu.be/ikdbhwa1o8U
