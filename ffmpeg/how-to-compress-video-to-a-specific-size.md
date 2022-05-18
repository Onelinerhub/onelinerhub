# How to compress video to a specific size

### In order to compress video to a specific size, first calculate target bitrate as `bitrate = target size / duration`. Then use this bitrate in the specified command. For example, we want video of `1Mb` in size and our target video is 1 minute and 22 seconds in length. Then we should use `1024/82 = 12k`:

```bash
ffmpeg -y -i in.mp4 -c:v libx264 -b:v 12k -pass 1 -f mp4 /dev/null
ffmpeg -i in.mp4 -c:v libx264 -b:v 12k -pass 2 out.mp4
```

- `-i in.mp4` - input video file
- `-c:v libx264` - use [H.264 codec](/ffmpeg/using-crf-with-h264-codec)
- `-b:v` - set video bitrate
- `12k` - use calculated value, not that final video weight more than `1Mb` because of additional audio channel data
- `-pass 1` - first pass to analyze video
- `-pass 2` - second pass to encode video using collected data


