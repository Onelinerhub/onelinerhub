# How to speed up video and audio

```bash
ffmpeg -i in.mp4 -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]" -map "[v]" -map "[a]" out.mp4

```

- `-i in.mp4` - input video file
- `-filter_complex` - applies specified video/audio complex filter
- `setpts=0.5*PTS` - will speed up video 2x
- `atempo=2.0` - will speed up audio 2x
- `-map "[v]" -map "[a]"` - map video and audio channels
- `out.mp4` - resulting video file

group: speed


