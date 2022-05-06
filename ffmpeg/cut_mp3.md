# How to cut MP3 based on start/end

```bash
ffmpeg -i in.mp3 -ss 10 -t 15 -acodec copy out.mp3
```

- `-i in.mp3` - input MP3 file
- `-ss 10` - start cutting after 10 seconds from the start
- `-t 15` - cut 15 seconds piece (final audio length will be 15 seconds)
- `out.mp3` - resulting MP3 file


link_youtube: https://youtu.be/_vlZDSKjzeI
