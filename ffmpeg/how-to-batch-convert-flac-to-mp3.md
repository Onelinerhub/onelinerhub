# How to batch convert FLAC to MP3

```bash
for i in $(ls *.flac); do ffmpeg -i $i ${i/flac/mp3}; done
```

- `for i in $(ls *.flac)` - bash loop to iterate over all `flac` files
- `-i $i` - use each found file as input
- `${i/flac/mp3}` - replace extension to `mp3` for output file

group: batch


