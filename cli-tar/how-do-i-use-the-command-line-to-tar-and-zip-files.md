# How do I use the command line to tar and zip files?
// plain

The command line can be used to tar and zip files using the `tar` and `gzip` commands. To tar a file, use the `tar` command followed by the `cvf` flags and the desired filename, e.g. `tar cvf mytarfile.tar myfile.txt`. This will create a tar file named `mytarfile.tar` containing the file `myfile.txt`. To zip the tar file, use the `gzip` command followed by the desired filename, e.g. `gzip mytarfile.tar`. This will create a zipped tar file named `mytarfile.tar.gz`.

## Example code


```
tar cvf mytarfile.tar myfile.txt
gzip mytarfile.tar
```

## Output example

```
mytarfile.tar.gz
```

## Code explanation

- `tar`: the command used to create a tar file
- `cvf`: flags used to create a tar file
- `mytarfile.tar`: the desired filename for the tar file
- `myfile.txt`: the file to be tarred
- `gzip`: the command used to zip a file
- `mytarfile.tar.gz`: the desired filename for the zipped tar file

## Helpful links
- [Gnu Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
- [Gzip Manual](https://www.gnu.org/software/gzip/manual/gzip.html)

onelinerhub: [How do I use the command line to tar and zip files?](https://onelinerhub.com/cli-tar/how-do-i-use-the-command-line-to-tar-and-zip-files)