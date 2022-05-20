# How to apply zoom-in effect to video

### This code **needs improvement**, help us and [edit it here](https://github.com/Onelinerhub/onelinerhub/blob/main/ffmpeg/how-to-apply-zoom-in-effect-to-video.md).

```ffmpeg
ffmpeg -i in.mp4 -vf "zoompan=z='min(max(zoom,pzoom)+0.0015,1.5)':d=0:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'" out.mp4
```

- `-i in.mp4` - input video file
- `zoompan` - filter to apply zoom-in effect
- `1.5` - zoom 1.5x
- `out.mp4` - resulting video file


link_youtube: https://youtu.be/cuam3SzMM3A
