# How do I download a file using Express.js?
// plain

To download a file using Express.js, you can use the `res.download` method. This method takes the path of the file as an argument and streams the file to the response object.

For example:

```javascript
app.get('/download', (req, res) => {
  const file = `${__dirname}/public/file.pdf`;
  res.download(file);
});
```

This code will send the file located at `/public/file.pdf` to the response object.

## Code explanation


- `app.get('/download', (req, res) => {`: This is the route definition. It defines the request URL and the callback function that will be called when the URL is requested.

- `const file = `${__dirname}/public/file.pdf`;`: This defines the path of the file to be downloaded.

- `res.download(file);`: This is the method that sends the file to the response object.

Here are some ## Helpful links

- [Express.js Documentation - res.download](https://expressjs.com/en/4x/api.html#res.download)
- [Node.js Documentation - fs.createReadStream](https://nodejs.org/api/fs.html#fs_fs_createreadstream_path_options)

onelinerhub: [How do I download a file using Express.js?](https://onelinerhub.com/expressjs/how-do-i-download-a-file-using-express-js)