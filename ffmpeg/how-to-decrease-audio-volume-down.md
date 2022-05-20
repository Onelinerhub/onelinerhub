# How to decrease audio volume down

```bash
ffmpeg -i in.mp3 -filter:a "volume=-10dB" out.mp3
```

- `-i in.mp3` - input MP3 file
- `-filter:a` - applies specified audio filter
- `volume=` - change volume level by specified amount
- `-10dB` - decrease volume by 10dB
- `out.mp3` - resulting file

group: volume


link_youtube: https://youtu.be/Fiz-ScpC2lg
