# How do I download and use the CLI version of Sed?
// plain

1. Download the source code for the CLI version of Sed from [GNU ftp](ftp://ftp.gnu.org/gnu/sed/).
2. Unpack the source code using your favorite unzip program.
3. Navigate into the source code directory and run `./configure` to configure the program for your system.
4. Run `make` to build the program.
5. Run `make install` to install the program.
6. Run `sed --help` to view the available options for using Sed.
7. To use Sed, you can run a command such as `sed 's/foo/bar/g' foo.txt` which will replace all instances of `foo` with `bar` in the file `foo.txt`.

Example code block:
```
$ sed 's/foo/bar/g' foo.txt
```

Output of example code:
```
bar
```

## Code explanation

- `sed`: The Sed command.
- `s/foo/bar/g`: The substitution command which replaces all instances of `foo` with `bar`.
- `foo.txt`: The file to apply the substitution to.

## Helpful links
- [GNU ftp](ftp://ftp.gnu.org/gnu/sed/)
- [Sed Tutorial](https://www.grymoire.com/Unix/Sed.html)

onelinerhub: [How do I download and use the CLI version of Sed?](https://onelinerhub.com/cli-sed/how-do-i-download-and-use-the-cli-version-of-sed)