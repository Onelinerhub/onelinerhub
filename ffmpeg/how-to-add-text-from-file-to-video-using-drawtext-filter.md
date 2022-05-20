# How to add text from file to video using drawtext filter

```bash
ffmpeg -i in.mp4 -vf "drawtext=x=10:y=20:fontsize=24:fontcolor=white:textfile=text.txt" -c:a copy out.mp4
```

- `-i in.mp4` - input video file
- `-vf` - apply specific video filters
- `drawtext=` - drawtext filter options
- `x=` - horizontal position in pixels from top left corner
- `y=` - vertical position in pixels from top left corner
- `fontsize` - size of the text to display
- `fontcolor` - color of the text
- `-c:a copy` - copy audio without converting
- `out.mp4` - resulting video file
- `textfile=` - path text file with text to add to video

group: drawtext


link_youtube: https://youtu.be/AbrPc06WXfE
