# How to reduce background audio noise using arnndn

```bash
git clone https://github.com/GregorR/rnnoise-models.git
ffmpeg -i in.mp3 -af "arnndn=m='rnnoise-models/somnolent-hogwash-2018-09-01/sh.rnnn'" out.mp3
```

- `ffmpeg` - name of the package to install
- `-i in.mp3` - input MP3 file
- `arnndn` - use neural networks noise reduction filter
- `m=` - set path to trained model file (downloaded from [github repo](https://github.com/GregorR/rnnoise-models))
- `out.mp3` - resulting file
- `GregorR/rnnoise-models.git` - github repo with trained NN models

group: noise


