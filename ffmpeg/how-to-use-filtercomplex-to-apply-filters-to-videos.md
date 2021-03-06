# How to use filter_complex to apply filters to videos

### When you have multiple inputs or you need to apply multiple filters, you can use `filter_complex`. This example resizes given image to `50x50` and places it (overlays) over given video:

```bash
ffmpeg -i in.mp4 -i in.png -filter_complex "[1]scale=50:50[in2];[0][in2]overlay" out.mp4
```

- `-i in.mp4` - first input (can be referred as `[0]`)
- `-i in.png` - second input (can be referred as `[1]`)
- `-filter_complex` - applies specified video/audio complex filter
- `[1]scale=50:50[in2]` - applies `scale` filter to input `[1]` (`in.png` image) and name the result as `[in2]` (so it can be referred later)
- `[0][in2]overlay` - applies overlay filter with inputs `[0]` (`in.mp4`) and `[in2]` (result of previous filtering)
- `out.mp4` - resulting video file


link_youtube: https://youtu.be/pBIPKn0bqCM
