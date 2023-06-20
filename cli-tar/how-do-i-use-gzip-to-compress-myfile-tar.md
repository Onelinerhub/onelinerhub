# How do I use gzip to compress myfile.tar?
// plain

1. To compress a file `myfile.tar` using gzip, use the following command:
```
gzip myfile.tar
```
This will create a new compressed file `myfile.tar.gz` in the same directory.
2. The `gzip` command uses the Lempel-Ziv (LZ77) algorithm to compress the file.
3. The `-v` option can be used to get verbose output about the compression process:
```
gzip -v myfile.tar
```
## Output example

```
myfile.tar:  78.1% -- replaced with myfile.tar.gz
```
4. The `-k` option can be used to keep the original file after compression:
```
gzip -k myfile.tar
```
5. The `-r` option can be used to recursively compress all files in a directory:
```
gzip -r mydirectory
```
6. To decompress a file, use the `gunzip` command:
```
gunzip myfile.tar.gz
```
7. For more information on the `gzip` command, see the [GNU gzip manual](https://www.gnu.org/software/gzip/manual/gzip.html).

onelinerhub: [How do I use gzip to compress myfile.tar?](https://onelinerhub.com/cli-tar/how-do-i-use-gzip-to-compress-myfile-tar)