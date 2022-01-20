# How to add user to sudoers

```bash
usermod -aG sudo user1
```

- `usermod` - utility to manage users
- `-aG` - appends specified user to specified group
- `sudo` - this group allows user to execute `sudo` command
- `user1` - username to add to sudoers


