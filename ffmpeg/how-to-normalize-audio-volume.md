# How to normalize audio volume

### To normalize automatically, use awesome [ffmpeg-normalize](/ffmpeg/how-to-automatically-normalize-audio-volume) tool. In order to normalize with native `ffmpeg`, you first need to detect volume detect `mean` and `max` volumes and then increase/decrease volume based on those values:

```bash
ffmpeg -i in.mp3 -filter:a volumedetect -f null /dev/null
ffmpeg -i in.mp3 -filter:a "volume=10dB" out.mp3
```

- `-i in.mp3` - input MP3 file
- `-filter:a` - applies specified audio filter
- `volumedetect` - detect `mean` and `max` audio volume for given file
- `volume=` - change volume level by specified amount
- `10dB` - increase volume by 10dB
- `out.mp3` - resulting file

group: volume

## Example: 
```bash
ffmpeg -i in.mp3 -filter:a volumedetect -f null /dev/null
```
```
...
[Parsed_volumedetect...] mean_volume: -24.1 dB
[Parsed_volumedetect...] max_volume: -10.7 dB
...
```

