# How can I troubleshoot when my CLI sed command is not working?
// plain

When troubleshooting a sed command that is not working, the following steps should be taken:

1. Check the syntax of the command. Make sure that the command is being written correctly and that all of the flags and parameters are being used correctly.

2. Check the input and output files. Make sure that the input file is in the correct format and that the output file is being written to the correct location.

3. Run the command with the `-n` flag. This flag will suppress the default output and will provide an error message if there is a problem with the command.

4. Check the `sed` man page. This will provide a detailed explanation of how `sed` works and the different flags and parameters that can be used.

5. Run the command with the `-n -e` flag. This will print out the commands being used and the line numbers that they are being applied to.

6. Check the `sed` regex documentation. This will provide a detailed explanation of the different regex syntaxes that can be used with `sed`.

7. Search for a specific error message. If the command is still not working, searching for the specific error message may provide more information about the issue.

Example code block:
```
sed -n -e 's/foo/bar/g' input.txt
```

Example output:
```
bar
```

onelinerhub: [How can I troubleshoot when my CLI sed command is not working?](https://onelinerhub.com/cli-sed/how-can-i-troubleshoot-when-my-cli-sed-command-is-not-working)