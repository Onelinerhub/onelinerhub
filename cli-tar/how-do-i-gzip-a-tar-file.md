# How do I gzip a tar file?
// plain

To gzip a tar file, you can use the following command:
```
tar -zcvf <output_file.tar.gz> <input_file.tar>
```
This command will create a gzipped tar file called `output_file.tar.gz` based on the `input_file.tar`. The flags used are:
- `z` for gzip compression
- `c` to create a new archive
- `v` for verbose output
- `f` to specify the output file

The output of the command will look like this:
```
input_file.tar
input_file.tar
input_file.tar
...
```

To uncompress the tar file, you can use the command:
```
tar -zxvf <input_file.tar.gz>
```
This will extract the files from the gzipped tar file. The flags used are:
- `z` for gzip decompression
- `x` to extract files from the archive
- `v` for verbose output
- `f` to specify the input file

The output of the command will look like this:
```
input_file.tar
input_file.tar
input_file.tar
...
```

## Helpful links
- [GNU tar manual](https://www.gnu.org/software/tar/manual/html_node/tar_93.html)
- [Gzip manual](https://www.gnu.org/software/gzip/manual/gzip.html)

onelinerhub: [How do I gzip a tar file?](https://onelinerhub.com/cli-tar/how-do-i-gzip-a-tar-file)