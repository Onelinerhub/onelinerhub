# Cut video based on start/end time

```bash
ffmpeg -i in.mp4 -ss 00:00:10 -t 00:01:30 -async 1 out.mp4
```

- `in.mp4` - input video file to cut from
- `-ss 00:00:10` - start cutting at 10 seconds
- `-t 00:01:30` - end cutting at 1 minute 30 seconds
- `out.mp4` - write result to this file


link_youtube: https://youtu.be/sYsID3aHCa4
