# Seeking video with "-ss" option

### This example will cut input video with `-ss` seeking and `-to` time limiting options:

```bash
ffmpeg -i in.mp4 -ss 00:00:05 -to 00:00:10 out.mp4
```

- `-i in.mp4` - input video file
- `-ss` - seeks 
- `00:00:05` - seek (set start point) to 5 seconds from the beginning of input video
- `-to` - end video on specified time
- `00:00:10` - resulting video will end on 10 seconds point of the original video (so will have `5 seconds` duration)
- `out.mp4` - resulting video file


