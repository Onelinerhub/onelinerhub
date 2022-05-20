# How to align text to center of the video using drawtext filter

```bash
ffmpeg -i in.mp4 -vf "drawtext=text='I am middle text':x=(w-text_w)/2:y=(h-text_h)/2:fontsize=24:fontcolor=white" -c:a copy out.mp4
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
- `(w-text_w)/2` - calculate `X` position of text based on video width (`w`) and text width (`text_w`), divided by 2
- `(h-text_h)/2` - calculate `Y` position of text based on video height (`h`) and text height (`text_h`), divided by 2

group: drawtext


link_youtube: https://youtu.be/Ajb4km5gIiU
