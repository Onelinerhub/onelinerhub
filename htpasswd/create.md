# Create new htpasswd file with username and password

```bash
htpasswd -c /dir/.htpasswd user1
```

- htpasswd - tool to manage encrypted users passwords
- -c - create new htpasswd file
- /dir/.htpasswd - path to the new password file
- user1 - add this user to the new password file (password will be asked after that)

group: add_pwd
