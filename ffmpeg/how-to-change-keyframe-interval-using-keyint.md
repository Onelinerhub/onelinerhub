# How to change keyframe interval using keyInt

```bash
ffmpeg -i in.mp4 -vcodec libx264 -x264-params keyint=5 -acodec copy out.mp4
```

- `-i in.mp4` - input video file
- `-vcodec libx264` - use H.264 video codec
- `keyint` - sets the number of frames inside GOP
- `5` - use maximum of 5 frames for each GOP, note that this is quite small amount, only for demo purposes
- `-acodec copy` - do not reencode audio, just copy it
- `out.mp4` - resulting video file


link_youtube: https://youtu.be/6MnJ-60qtvY
