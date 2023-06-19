# How can I configure Express.js to use Nginx as a reverse proxy?
// plain

To configure Express.js to use Nginx as a reverse proxy, you need to set up Nginx as a reverse proxy server and configure it to forward requests to your Express.js application.

First, install Nginx and configure it as a reverse proxy server. In its configuration file, add the following code block:

```
server {
    listen 80;
    server_name example.com;
    location / {
        proxy_pass http://localhost:3000;
    }
}
```

This will tell Nginx to listen on port 80 and forward all requests to `example.com` to `localhost:3000`, where your Express.js application is running.

Next, in your Express.js application, set the `trust proxy` setting to `true` to tell Express.js that it is running behind a reverse proxy.

```
app.set('trust proxy', true);
```

Finally, make sure that your application is running on `localhost:3000` and restart Nginx.

## Code explanation


1. `listen 80;`: tells Nginx to listen on port 80.
2. `server_name example.com;`: tells Nginx to forward requests to `example.com` to the specified location.
3. `proxy_pass http://localhost:3000;`: tells Nginx to forward requests to `localhost:3000`.
4. `app.set('trust proxy', true);`: tells Express.js that it is running behind a reverse proxy.

## Helpful links

- [Nginx Reverse Proxy](https://www.nginx.com/resources/admin-guide/reverse-proxy/)
- [Express.js Trust Proxy Setting](https://expressjs.com/en/guide/behind-proxies.html)

onelinerhub: [How can I configure Express.js to use Nginx as a reverse proxy?](https://onelinerhub.com/expressjs/how-can-i-configure-express-js-to-use-nginx-as-a-reverse-proxy)