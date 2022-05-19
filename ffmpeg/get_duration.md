# Get duration of video

### Use `ffprobe` (included with ffmpeg) to get the duration:

```bash
ffprobe EXAMPLE.mp4 -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 -sexagesimal
```

- ``ffprobe EXAMPLE.mp4`` - ffprobe the file
- ``-v quiet`` - reduce the amount of output
- ``-show_entries format=duration`` - return only the 'duration' entry
- ``-of default=noprint_wrappers=1:nokey=1`` - remove the '[FORMAT]' wrappers by setting the format
- ``-sexagesimal`` - format the time to be in hours:minutes:seconds:milliseconds

group: duration

## Example: 
```bash
ffprobe EXAMPLE.mp4 -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 -sexagesimal
```
```
0:00:20.000000
```

link_youtube: https://youtu.be/3_RrW-AlroI
