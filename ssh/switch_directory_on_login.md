# Switch to a specific directory right on login

```bash
ssh -t user@server.com "cd /path/to/dir; bash --login"
```

- -t  - will allocate pseudo terminal = allow us to launch our own bash session
- user@server.com - remote user and server address
- cd /path/to/dir - switch current directory to the needed one
- bash --login - launch bash session after switching to the directory
