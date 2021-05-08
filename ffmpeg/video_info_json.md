# Get video information in JSON format

```bash
ffprobe -v quiet -print_format json -show_format -show_streams in.mp4
```

- -v quiet - skip version details printing
- -print_format json - will show everything in JSON
- in.mp4 - video file to show info about
- -show_format -show_streams - will show info about video format and streams
