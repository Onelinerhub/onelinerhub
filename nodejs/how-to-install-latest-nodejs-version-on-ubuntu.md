# How to install latest Node.js version on Ubuntu

```bash
curl -fsSL https://deb.nodesource.com/setup_current.x | sudo -E bash -
sudo apt install -y nodejs
```

- `setup_current.x` - installation script for latest current Node.js release
- `apt install -y nodejs` - will automatically install given package

group: install

## Example: 
```bash
node -v
```
```
v18.7.0
```

