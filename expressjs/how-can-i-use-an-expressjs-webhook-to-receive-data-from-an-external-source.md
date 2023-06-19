# How can I use an ExpressJS webhook to receive data from an external source?
// plain

Using ExpressJS webhooks to receive data from an external source is a simple process.

The first step is to create a route in your ExpressJS app that will handle the incoming data. For example:

```javascript
app.post('/webhook', (req, res) => {
  // Handle incoming data
});
```

Once the route is created, the next step is to configure the external source to send data to the route. This may involve providing the external source with the URL of the route, or other authentication credentials.

After the external source is configured, it will send data to the route when triggered. The data will be available in the `req` parameter of the route. For example:

```javascript
app.post('/webhook', (req, res) => {
  console.log(req.body);
});

// Output: { name: 'John', age: 30 }
```

The data can then be handled as needed. This may involve storing the data in a database, or sending a response back to the external source.

Once the data is handled, the response should be sent to the external source. This is typically done by setting the status code and sending a response body. For example:

```javascript
app.post('/webhook', (req, res) => {
  // Handle incoming data

  res.status(200).send({ message: 'Data received' });
});
```

This is a basic example of how to use an ExpressJS webhook to receive data from an external source.

## Helpful links
- [ExpressJS documentation](https://expressjs.com/en/4x/api.html)
- [Webhooks tutorial](https://www.digitalocean.com/community/tutorials/how-to-create-and-configure-webhooks-on-github)

onelinerhub: [How can I use an ExpressJS webhook to receive data from an external source?](https://onelinerhub.com/expressjs/how-can-i-use-an-expressjs-webhook-to-receive-data-from-an-external-source)