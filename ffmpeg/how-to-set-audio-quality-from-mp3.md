# How to set audio quality for MP3

### In order to reduce audio quality, try reducing bitrate of your audio (channel):

```ffmpeg
ffmpeg -i in.mp3 -codec:a libmp3lame -qscale:a 2 out.mp3
```

- `-i in.mp3` - input MP3 file
- `-codec:a` - set specified audio codec
- `libmp3lame` - this library allows highly efficient variable bitrate audio encoding
- `-qscale:a` - set audio quality level
- `2` - use high quality (`0` for best, `9` for worst)
- `out.mp3` - resulting file

group: audio_quality


