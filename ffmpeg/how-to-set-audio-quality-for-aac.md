# How to set audio quality for AAC

### In order to reduce audio quality, try reducing bitrate of your audio (channel):

```ffmpeg
ffmpeg -i in.mp4 -c:a aac -b:a 192k out.m4a
```

- `-i in.mp3` - input MP3 file
- `-codec:a` - set specified audio codec
- `-c:a aac` - use [`AAC` codec](/ffmpeg/encode-mp3-to-aac) for audio
- `-b:a` - set audio quality by setting bitrate (lower - worse, bigger - better)
- `192k` - use average quality level
- `out.m4a` - resulting `aac` file

group: audio_quality


