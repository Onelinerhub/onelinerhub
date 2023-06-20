# How can I use SED in a Windows command line interface?
// plain

SED is a command line tool for stream editing and can be used in a Windows command line interface. To use SED, you will need to install the GNU version of SED for Windows.

Once installed, you can use SED in a Windows command line interface by using the following syntax:

```
sed [options] [script] [inputfile]
```

For example, the following command will replace all occurrences of the word "apple" with the word "orange" in the file "fruit.txt":

```
sed s/apple/orange/g fruit.txt
```

The output of this command would be the contents of the "fruit.txt" file with all occurrences of the word "apple" replaced with the word "orange".

The parts of the command are:

* `sed` - the command to invoke SED
* `s/apple/orange/g` - the script to execute, which replaces all occurrences of "apple" with "orange"
* `fruit.txt` - the input file

## Helpful links

* [GNU SED for Windows](https://sourceforge.net/projects/gnuwin32/files/sed/)
* [SED Command Tutorial](https://www.guru99.com/sed-command-unix-linux.html)

onelinerhub: [How can I use SED in a Windows command line interface?](https://onelinerhub.com/cli-sed/how-can-i-use-sed-in-a-windows-command-line-interface)