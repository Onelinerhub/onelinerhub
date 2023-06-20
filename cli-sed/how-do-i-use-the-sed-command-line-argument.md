# How do I use the sed command line argument?
// plain

The sed command line argument is a powerful tool for manipulating text files. It allows you to edit files without actually opening them. To use the sed command line argument, you must specify the file you wish to edit, followed by an argument of the changes you wish to make.

For example, to replace all occurrences of the word “apple” with the word “orange” in a file named “fruits.txt”, you would use the following command:

```
sed 's/apple/orange/g' fruits.txt
```

The output of the command would be the contents of the file “fruits.txt” with all occurrences of the word “apple” replaced with the word “orange”.

The command consists of several parts:

* `sed` - the command itself
* `s/apple/orange/g` - a substitution command, instructing sed to replace all occurrences of the word “apple” with the word “orange”
* `fruits.txt` - the file to be edited

For more information on the sed command line argument, see the following links:

* [GNU sed Manual](https://www.gnu.org/software/sed/manual/sed.html)
* [Sed Tutorial](https://www.grymoire.com/Unix/Sed.html)

onelinerhub: [How do I use the sed command line argument?](https://onelinerhub.com/cli-sed/how-do-i-use-the-sed-command-line-argument)