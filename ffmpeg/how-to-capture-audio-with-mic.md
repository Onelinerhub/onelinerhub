# How to capture audio with mic

```bash
ffmpeg -f alsa -i hw:1 out.wav
```

- `-f alsa` - selects `ALSA` input device which allows capturing audio
- `-i` - specify input device (microphone in our case)
- `hw:1` - use first mic available
- `out.wav` - resulting file with captured audio

group: capture


