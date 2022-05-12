# How to reduce background audio noise using afftdn

```bash
ffmpeg -i in.mp3 -af "afftdn=nr=10:nf=-30:tn=1" out.mp3
```

- `ffmpeg` - name of the package to install
- `-i in.mp3` - input MP3 file
- `-af` - apply specified audio filter
- `afftdn` - filter for denoising audio samples
- `nr=10` - reduce noise by 10dB (tune this for better results)
- `nf=-30` - use noise floor (level) as -30dB (tune this for better results)
- `tn=1` - noise level will be tracked and gradually changed during processing
- `out.mp3` - resulting file

group: noise


