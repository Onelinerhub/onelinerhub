# How to convert video to GIF animation

```bash
ffmpeg -i in.mp4 -vf "select='not(mod(n,10))',setpts='N/(30*TB)'" -f image2 /tmp/in%03d.png
ffmpeg -f image2 -framerate 10 -i /tmp/in%03d.png out.gif
rm -rf /tmp/in*
```

- `-i in.mp4` - input video file
- `-vf` - apply specific video filters
- `not(mod(n,10))` - create still image every 10 frames
- `-f image2` - format to operate lists of images
- `/tmp/in%03d.png` - save captured image stills to temporary `png` files
- ` -framerate 10` - resulting animation frame rate (`10` frames per second)
- `out.gif` - resulting `GIF` animation file
- `rm -rf /tmp/in*` - clear temporary files

group: gif


