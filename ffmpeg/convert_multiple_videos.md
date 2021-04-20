# How to convert multiple files

Will convert all ```mp4``` files to ```mkv``` files.

```bash
for i in *.mp4; do ffmpeg -i "$i" "${i%.*}.mkv"; done
```
