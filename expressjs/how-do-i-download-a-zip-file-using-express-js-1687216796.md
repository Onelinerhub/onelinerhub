# How do I download a zip file using Express.js?
// plain

To download a zip file using Express.js, you will need to use the [express.static](https://expressjs.com/en/starter/static-files.html) middleware.

First, you'll need to create a route in the Express server that will serve the zip file:

```javascript
// Serve zip file
app.get('/download', function(req, res){
  res.download('/path/to/zipfile.zip');
});
```

Then, you'll need to use the express.static middleware to make the zip file accessible to the client.

```javascript
// Serve static files
app.use(express.static(__dirname + '/public'));
```

Finally, you can send an AJAX request from the client side to the route you created to trigger the download:

```javascript
// Send AJAX request
$.ajax({
  url: '/download',
  type: 'GET',
  success: function(data) {
    console.log('Download successful!');
  }
});
```

The client will then receive the zip file, which can be opened and used as needed.

## Code explanation


1. Create a route in the Express server that will serve the zip file:
    ```javascript
    // Serve zip file
    app.get('/download', function(req, res){
      res.download('/path/to/zipfile.zip');
    });
    ```
2. Use the express.static middleware to make the zip file accessible to the client:
    ```javascript
    // Serve static files
    app.use(express.static(__dirname + '/public'));
    ```
3. Send an AJAX request from the client side to the route you created to trigger the download:
    ```javascript
    // Send AJAX request
    $.ajax({
      url: '/download',
      type: 'GET',
      success: function(data) {
        console.log('Download successful!');
      }
    });
    ```

## Helpful links
- [Express.js static middleware](https://expressjs.com/en/starter/static-files.html)
- [jQuery AJAX](https://api.jquery.com/jquery.ajax/)

onelinerhub: [How do I download a zip file using Express.js?](https://onelinerhub.com/expressjs/how-do-i-download-a-zip-file-using-express-js-1687216796)