# How to batch convert MKV to MP4

```bash
for i in $(ls *.mkv); do ffmpeg -i $i ${i/mkv/mp4}; done
```

- `for i in $(ls *.mkv)` - bash loop to iterate over all `mkv` files
- `-i $i` - use each found video as input
- `${i/mkv/mp4}` - replace extension to `mp4` for output file

group: batch


