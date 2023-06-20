# How can I fix the "cli sed not found" error?
// plain

The "cli sed not found" error is usually caused by a missing or incorrect configuration of the `sed` command on the command line.

To fix this error, you can try the following steps:

1. Check if `sed` is installed on your system:
```
which sed
```

2. If `sed` is not installed, install it using your system's package manager (e.g. `apt` or `yum`).

3. If `sed` is installed, check if the path to `sed` is correctly configured in your `PATH` environment variable.

4. If the path to `sed` is not correctly configured, add the path to `sed` to your `PATH` environment variable.

5. Restart your terminal session to apply the changes to your `PATH` environment variable.

6. Check if `sed` is now working correctly:
```
which sed
```

7. If `sed` is still not found, you may need to reinstall `sed` or check the permissions of the `sed` executable.

For more information, see the following links:
- [How to Install the sed Command on Linux](https://linuxize.com/post/how-to-install-sed-command-on-linux/)
- [How to Set Environment Variables in Linux](https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/)

onelinerhub: [How can I fix the "cli sed not found" error?](https://onelinerhub.com/cli-sed/how-can-i-fix-the--cli-sed-not-found--error)