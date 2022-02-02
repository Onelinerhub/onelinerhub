# ubuntu cli install deb

```bash
sudo apt install -y /path/to/some.deb
```

- `sudo` - execute command as super user (root)
- `apt install` - installs specified package on Ubuntu
- `-y` - will install everything with no questions
- `/path/to/some.deb` - path to `deb` file to install

## Example: 
```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install ./google-chrome-stable_current_amd64.deb
```

