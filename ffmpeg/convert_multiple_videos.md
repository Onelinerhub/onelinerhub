# How to convert multiple files

```bash
for i in *.mp4; do ffmpeg -i "$i" "${i%.*}.mkv"; done
```

- *.mp4 - will select all mp4 files in current folder
- ${i%.*}.mkv - will convert everything to mkv (change extension automatically)
