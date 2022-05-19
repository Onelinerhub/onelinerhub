# How to detect audio volume level

```bash
ffmpeg -hide_banner -i in.mp3 -filter:a volumedetect -f null /dev/null
```

- `-i in.mp3` - input MP3 file
- `-filter:a` - applies specified audio filter
- `volumedetect` - detect `mean` and `max` audio volume for given file
- `-f null /dev/null` - used to hide errors

group: volume

## Example: 
```bash
ffmpeg -hide_banner -i in.mp3 -filter:a volumedetect -f null /dev/null
```
```
...
[Parsed_volumedetect...] mean_volume: -24.1 dB
[Parsed_volumedetect...] max_volume: -10.7 dB
...
```

