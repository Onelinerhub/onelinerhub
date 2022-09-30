# How to init Node.js project with NPM

```bash
mkdir mynode && cd mynode
npm init --yes
```

- `npm` - Node.js package manager
- `init` - inits new package configuration
- `mynode` - new project directory name 

group: npm

## Example: 
```bash
mkdir mynode && cd mynode
npm init --yes
cat package.json
```
```
{
  "name": "mynode",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

link_youtube: https://youtu.be/O0-BCgRKaas
