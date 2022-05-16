# How to change font of text using drawtext filter

```bash
ffmpeg -i in.mp4 -vf "drawtext=text='Some text':x=10:y=20:fontsize=24:fontcolor=white:fontfile=font.ttf" -c:a copy out.mp4
```

- `-i in.mp4` - input video file
- `-vf` - apply specific video filters
- `drawtext=` - drawtext filter options
- `text=` - text to draw
- `x=` - horizontal position in pixels from top left corner
- `y=` - vertical position in pixels from top left corner
- `fontsize` - size of the text to display
- `fontcolor` - color of the text
- `-c:a copy` - copy audio without converting
- `out.mp4` - resulting video file
- `fontfile=` - path to `TTF` file to use 

group: drawtext


