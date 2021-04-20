# Concatenate several videos 

Will concatenate ```part1.mkv``` and ```part2.mkv```, result will be written to ```output.mkv```.

```bash
ffmpeg -i part1.mkv -i part2.mkv -filter_complex "[0:v] [0:a] [1:v] [1:a] concat=n=2:v=1:a=1 [v] [a]" -map "[v]" -map "[a]" output.mkv
```
