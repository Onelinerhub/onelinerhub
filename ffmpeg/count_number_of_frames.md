# Get the number of frames in video

Will print the number of frames in ```in.mp4```.

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=nb_frames -of default=nokey=1:noprint_wrappers=1 in.mp4
```
