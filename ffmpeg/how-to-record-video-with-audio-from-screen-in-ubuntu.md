# How to record video with audio from screen in Ubuntu

### This command will start capturing, press `Ctrl+C` when finished:

```bash
ffmpeg -video_size 1280x720 -framerate 25 -f x11grab -i :0.0+100,200 -f alsa -ac 2 -i hw:0 out.mp4
```

- `-video_size` - resulting video size to capture
- `1280x720` - capture `720p` video
- `-framerate 25` - set frame rate to `25` per second
- `-f x11grab` - grab video from `X11` device
- `-i :0.0+100,200` - set coordinates of top left corner to capture video (`100 pixels` horizontally and `200 pixels` vertically)
- `-f alsa` - capture audio from `ALSA` device
- `-ac 2` - set number of audio channels
- `-i hw:0` - hardware device ([sound card](/ffmpeg/how-to-list-recording-sound-devices-on-pc-in-ubuntu)) to capture audio from
- `out.mp4` - resulting video file

group: capture


