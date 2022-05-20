# How to batch convert WAV to MP3

```bash
for i in $(ls *.wav); do ffmpeg -i $i ${i/wav/mp3}; done
```

- `for i in $(ls *.wav)` - bash loop to iterate over all `wav` files
- `-i $i` - use each found file as input
- `${i/wav/mp3}` - replace extension to `mp3` for output file

group: batch


link_youtube: https://youtu.be/N-TyMiI0tB4
