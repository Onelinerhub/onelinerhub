# How can I view my command line sed history?
// plain

The command line history of sed can be viewed by using the `sed -n -e 'H;${x;s/\n/ /g;s/^,*//;s/,*$//;p;}' ~/.bash_history | sed -e 's/^[ \t]*//'` command. This command prints the entire command line history of sed, including all the commands, options, and arguments used.

For example, to view the command line history of sed from the last 7 days, the following command can be used:

```
sed -n -e 'H;${x;s/\n/ /g;s/^,*//;s/,*$//;p;}' ~/.bash_history | sed -e 's/^[ \t]*//' | grep -E "^sed .* [0-9]{4}-[0-9]{2}-[0-9]{2}"
```

The command is composed of several parts:

* `sed -n -e 'H;${x;s/\n/ /g;s/^,*//;s/,*$//;p;}' ~/.bash_history` – This part of the command prints the entire command line history of sed, including all the commands, options, and arguments used.
* `sed -e 's/^[ \t]*//'` – This part of the command removes any leading whitespace.
* `grep -E "^sed .* [0-9]{4}-[0-9]{2}-[0-9]{2}"` – This part of the command filters the command line history of sed to only display commands from the last 7 days.

## Helpful links

* [Sed Command Tutorial](https://www.tutorialspoint.com/unix_commands/sed.htm)
* [Grep Command Tutorial](https://www.tutorialspoint.com/unix_commands/grep.htm)

onelinerhub: [How can I view my command line sed history?](https://onelinerhub.com/cli-sed/how-can-i-view-my-command-line-sed-history)