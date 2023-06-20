# How can I configure Vue.js to use Nginx?
// plain

To configure Vue.js to use Nginx, you need to do the following:

1. Create a Nginx configuration file `vue-project.conf` with the following contents:
```
server {
    listen       80;
    server_name  localhost;

    # Vue.js root directory
    root         /www/vue-project;

    # Serve static files
    location / {
        try_files $uri $uri/ /index.html;
    }
}
```
2. Save the file in the `/etc/nginx/conf.d/` directory.
3. Reload Nginx configuration with `sudo nginx -s reload`.
4. Open `localhost` in a web browser to view your Vue.js project.

## Helpful links
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Vue.js Documentation](https://vuejs.org/v2/guide/)

onelinerhub: [How can I configure Vue.js to use Nginx?](https://onelinerhub.com/vue.js/how-can-i-configure-vue-js-to-use-nginx)