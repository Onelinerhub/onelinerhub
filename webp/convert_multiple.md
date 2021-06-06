# Convert multiple images to WEBP

```bash
for f in *.jpg; do cwebp -q 90 "$f" -o "${f%.jpg}.webp"; done
```

- for f in *.jpg - loop through all ```jpg``` files in current directory
- cwebp -q 90 "$f" - converts image to webp with good quality
- ${f%.jpg}.webp" - output images will have ```webp``` extension
