# How can I use a variable with the sed command line tool?
// plain

The sed command line tool can be used to perform text manipulation on a file or stream. To use a variable with the sed command line tool, you can use the -e (--expression) option. The -e option allows you to pass an expression to sed, which can include a variable. For example:

```
my_var="hello"
sed -e "s/world/$my_var/" test.txt
```

The example above replaces the word "world" with the contents of the variable `my_var` in the file `test.txt`.

The parts of the code are as follows:

* `my_var="hello"` - this sets the variable `my_var` to the value `hello`
* `sed -e "s/world/$my_var/" test.txt` - this runs the sed command, using the expression `s/world/$my_var/` on the file `test.txt`

## Helpful links
* [Sed Manual](https://www.gnu.org/software/sed/manual/sed.html)
* [Sed Tutorial](https://www.grymoire.com/Unix/Sed.html)

onelinerhub: [How can I use a variable with the sed command line tool?](https://onelinerhub.com/cli-sed/how-can-i-use-a-variable-with-the-sed-command-line-tool)