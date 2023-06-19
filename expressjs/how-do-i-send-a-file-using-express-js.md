# How do I send a file using Express.js?
// plain

To send a file using Express.js, you can use the `sendFile` method. This method takes in the path of the file you want to send as its first argument.

For example:
```
app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});
```
This will send the `index.html` file located in the same directory as the script.

The `sendFile` method also takes an optional options object as its second argument. This object can be used to set the `root` and `dotfiles` properties. The `root` property is used to set the root directory from which files are served, and the `dotfiles` property is used to specify if dotfiles should be served or not.

For example:
```
app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html', {
    root: '/home/user/files',
    dotfiles: 'deny'
  });
});
```
This will send the `index.html` file located in the `/home/user/files` directory, and will deny any requests for dotfiles.

## Helpful links
- [Express.js Documentation - `res.sendFile()`](https://expressjs.com/en/api.html#res.sendFile)
- [Express.js Documentation - `res.sendFile()` Options](https://expressjs.com/en/4x/api.html#res.sendFile)

onelinerhub: [How do I send a file using Express.js?](https://onelinerhub.com/expressjs/how-do-i-send-a-file-using-express-js)