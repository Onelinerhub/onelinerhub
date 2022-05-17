# How to record video from screen

### This command will start capturing, press `Ctrl+C` when finished:

```bash
ffmpeg -video_size 1280x720 -framerate 25 -f x11grab -i :0.0+100,200 out.mp4
```


group: capture


