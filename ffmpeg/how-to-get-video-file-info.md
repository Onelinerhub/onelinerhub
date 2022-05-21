# How to get video file info

### Just ignore `At least one output file must be specified` error at the bottom of the output:

```bash
ffmpeg -hide_banner -i in.mp4
```

- `-i in.mp4` - input video file to get info for
- `-hide_banner` - hide generic program options

group: info

## Example: 
```bash
ffmpeg -hide_banner -i in.mp4
```
```
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'in.mp4':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    encoder         : Lavf58.76.100
  Duration: 00:01:22.80, start: 0.000000, bitrate: 212 kb/s
  Stream #0:0(und): Video: h264 (High) (avc1 / 0x31637661), yuv420p(tv, bt709), 1920x1080 [SAR 1:1 DAR 16:9], 75 kb/s, 30 fps, 30 tbr, 15360 tbn, 60 tbc (default)
    Metadata:
      handler_name    : VideoHandler
      vendor_id       : [0][0][0][0]
  Stream #0:1(und): Audio: aac (LC) (mp4a / 0x6134706D), 48000 Hz, stereo, fltp, 128 kb/s (default)
    Metadata:
      handler_name    : SoundHandler
      vendor_id       : [0][0][0][0]
```

link_youtube: https://youtu.be/IHv9SRVWRHg
