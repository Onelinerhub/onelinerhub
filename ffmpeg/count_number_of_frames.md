# Get the number of frames in video

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=nb_frames -of default=nokey=1:noprint_wrappers=1 in.mp4
```

- -v error - will output only errors, leaving clean output
- -select_streams v:0 - first video stream will be chosen
- -show_entries stream=nb_frames - asks to show us number of frames
- -of default=nokey=1:noprint_wrappers=1 - will print only number and skipp everything else
- in.mp4 - input file which we're counting frames for
