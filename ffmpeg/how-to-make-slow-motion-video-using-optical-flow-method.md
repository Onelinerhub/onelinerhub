# How to make slow motion video using optical flow method

```bash
ffmpeg -i in.mp4 -filter:v "setpts=2*PTS" tmp.mp4
ffmpeg -i tmp.mp4 -filter:v "minterpolate='mi_mode=mci:mc_mode=aobmc:vsbmc=1:fps=120'" out.mp4
```

- `-i in.mp4` - input video file
- `-filter:v` - apply specified video filter
- `setpts=2*PTS` - setpts filter will slow down video speed to half of original speed
- `tmp.mp4` - temporary slow video that needs to be improved
- `minterpolate` - motion interpolation filter to smooth out temporary video
- `fps=120` - frame rate for resulting video
- `out.mp4` - resulting video file

group: speed


