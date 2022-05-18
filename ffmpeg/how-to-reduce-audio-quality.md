# How to reduce audio quality

### In order to reduce audio quality, try reducing bitrate of your audio (channel):

```ffmpeg
ffmpeg -i in.mp3 -b:a 32k out.mp3
```

- `-i in.mp3` - input MP3 file
- `-b:a` - set audio quality by setting bitrate (lower - worse, bigger - better)
- `32k` - set poor quality, (use at least `128k` for average quality)
- `out.mp3` - resulting file

group: audio_quality


