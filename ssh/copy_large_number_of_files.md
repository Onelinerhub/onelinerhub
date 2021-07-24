# Quickly copy large number of files

```bash
tar czf - file1 dir2 | ssh user@server.com "cd /path && tar xvzf -"
```

- tar czf - - create gzipped tar and send result to output
- file1 dir2 - list of files or directories to gzip (`file1` and `dir2` in our case)
- | - send output from the left command to the right
- ssh user@server.com - remote user and server address
- cd /path - go to the directory we want to copy file to
- tar xvzf - - ungzip and untar files from input (sent by local tar command)
