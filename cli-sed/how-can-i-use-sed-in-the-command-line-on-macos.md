# How can I use sed in the command line on macOS?
// plain

Sed is a powerful command line tool that can be used to manipulate text on macOS. It is part of the GNU Core Utilities package, which is included in macOS.

To use sed in the command line, you can type `sed` followed by an expression that tells it what to do. For example, to replace all occurrences of the word "cat" with the word "dog", you can type:
```
sed 's/cat/dog/g'
```
This command will output the text with all occurrences of "cat" replaced with "dog".

The syntax for sed is as follows:
* `s` - substitute the following characters
* `/` - the delimiter for the characters to be replaced
* `cat` - the text to be replaced
* `/` - the delimiter for the replacement text
* `dog` - the replacement text
* `/g` - the global flag, which tells sed to replace all occurrences of the text

For more information on using sed in the command line, see the [GNU Sed Manual](https://www.gnu.org/software/sed/manual/sed.html).

onelinerhub: [How can I use sed in the command line on macOS?](https://onelinerhub.com/cli-sed/how-can-i-use-sed-in-the-command-line-on-macos)