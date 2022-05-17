# How to slow down audio

```ffmpeg
ffmpeg -i in.mp3 -filter:a "atempo=0.5" -vn out.mp3
```

- `-i in.mp3` - input MP3 file
- `-filter:a` - applies specified audio filter
- `atempo` - allows to change speed of audio (allows values from `0.5` to `2.0`)
- `0.5` - slows down audio speed twice
- `-vn` - skip video (process only audio)
- `out.mp3` - resulting file

group: audio_speed


