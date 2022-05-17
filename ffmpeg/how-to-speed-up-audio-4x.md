# How to speed up audio 4x

### Since `atempo` filter allows max `2x` speed increase, we use multiple `atempo` filters to bypass that limit:

```ffmpeg
ffmpeg -i in.mp3 -filter:a "atempo=2.0,atempo=2.0" -vn out.mp3
```

- `-i in.mp3` - input MP3 file
- `-filter:a` - applies specified audio filter
- `atempo` - allows to change speed of audio (allows values from `0.5` to `2.0`)
- `2.0` - speeds up audio speed twice
- `-vn` - skip video (process only audio)
- `out.mp3` - resulting file

group: audio_speed


