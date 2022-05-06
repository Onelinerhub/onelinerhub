# Create video thumbnail using ffmpegthumbnailer

```bash
ffmpegthumbnailer -i in.mp4 -o out.jpg -s 0 -t 10% -q 10
```

- `-i in.mp4` - input video file
- `-o out.jpg` - output image thumbnail
- `-s 0` - uses the same file dimensions as video. Use any number for different size (e.g. 128 or 512).
- `-t 10%` - thumbnail will be made at 10% of video length. You can also use time format hh:mm:ss.
- `-q 10` - best image quality possible. Available values are 1...10.

group: video_thumbnail


link_youtube: https://youtu.be/8xlsKy0zfr4
