# How to split video into multiple parts 

### At the moment, the only reliable option is to manually call corresponding commands to cut off parts from the original video. In this example we cut 3 video parts 5-seconds length each:

```bash
ffmpeg -i in.mp4 -ss 0  -t 5 p1.mp4
ffmpeg -i in.mp4 -ss 5  -t 5 p2.mp4
ffmpeg -i in.mp4 -ss 10 -t 5 p3.mp4
# ...
```

- `-i in.mp4` - input video file
- `-ss` - set start position (in seconds) to cut the part from source video
- `-t` - set resulting video part length (in seconds)
- `p1.mp4` - name of the first video part


