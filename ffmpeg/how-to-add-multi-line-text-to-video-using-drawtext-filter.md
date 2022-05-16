# How to add multi-line text to video using drawtext filter

### In order to add multiple lines of text to video, [load text from file](/ffmpeg/how-to-add-text-from-file-to-video-using-drawtext-filter) or use multiple `drawtext` filters (separated by commas):

```bash
ffmpeg -i in.mp4 -vf "drawtext=text='Hi everyone':x=10:y=10:fontsize=24:fontcolor=white,drawtext=text='Next line is here':x=10:y=30:fontsize=24:fontcolor=white" -c:a copy out.mp4
```

- `-i in.mp4` - input video file
- `-vf` - apply specific video filters
- `drawtext=` - drawtext filter options
- `text=` - text to draw
- `x=10` - horizontal position in pixels from top left corner
- `y=10` - vertical position in pixels from top left corner
- `fontsize` - size of the text to display
- `fontcolor` - color of the text
- `-c:a copy` - copy audio without converting
- `out.mp4` - resulting video file

group: drawtext


