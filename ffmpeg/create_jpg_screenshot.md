# Create JPG screenshot from a video at a specific time

```bash
ffmpeg -accurate_seek -ss 00:04:50 -i in.mp4 -frames:v 1 -qscale:v 2 out.jpg
```

- `-accurate_seek -ss 00:04:50` - take screenshot at 4 minutes 50 seconds
- `-i in.mp4` - input video file
- `-frames:v 1` - make screenshot of only 1 frame
- `-qscale:v 2` - image of the best quality possible (```2...31``` for goot to worst quality)
- `out.jpg` - output screenshot file

group: video_thumbnail


link_youtube: https://youtu.be/NIQ-3XmBq0M
