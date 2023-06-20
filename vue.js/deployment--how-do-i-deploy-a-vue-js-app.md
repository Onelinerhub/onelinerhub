# deployment

How do I deploy a Vue.js app?
// plain

Deploying a Vue.js app is a relatively simple process. First, you need to build the app using the `npm run build` command. This will generate a `dist` folder with all the static files needed for deployment.

Next, you need to configure your web server to serve the static files. For example, if you are using Apache, you can add the following configuration to your `.htaccess` file:

```
RewriteEngine On
RewriteBase /
RewriteRule ^index\.html$ - [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.html [L]
```

This will make sure that all requests are redirected to the `index.html` file in the `dist` folder.

Finally, you need to upload the `dist` folder to your web server and you're done.

Parts of the code:

- `RewriteEngine On`: enables the Apache rewrite engine
- `RewriteBase /`: sets the base directory for the rewrite rules
- `RewriteRule ^index\.html$ - [L]`: redirects requests for `index.html` to itself
- `RewriteCond %{REQUEST_FILENAME} !-f`: checks if the requested file is not a regular file
- `RewriteCond %{REQUEST_FILENAME} !-d`: checks if the requested file is not a directory
- `RewriteRule . /index.html [L]`: redirects all requests to `index.html`

## Helpful links

- [Vue.js deployment guide](https://vuejs.org/v2/guide/deployment.html)
- [Apache .htaccess tutorial](https://www.tutorialspoint.com/apache_web_server/apache_web_server_htaccess_files.htm)

onelinerhub: [deployment

How do I deploy a Vue.js app?](https://onelinerhub.com/vue.js/deployment--how-do-i-deploy-a-vue-js-app)