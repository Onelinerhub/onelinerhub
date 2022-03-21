# Configure XSS protection

### This is a [recommended list of security headers](https://webdock.io/en/docs/how-guides/security-guides/how-to-configure-security-headers-in-nginx-and-apache) to protect your app with Nginx:

```nginx
server {
  location / {
    add_header Strict-Transport-Security 'max-age=31536000; includeSubDomains; preload';
    add_header Content-Security-Policy "default-src 'self'; font-src *;img-src * data:; script-src *; style-src *";
    add_header X-XSS-Protection "1; mode=block";
    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-Content-Type-Options nosniff;
    add_header Referrer-Policy "strict-origin";
    add_header Permissions-Policy "geolocation=(),midi=(),sync-xhr=(),microphone=(),camera=(),magnetometer=(),gyroscope=(),fullscreen=(self),payment=()";
  }
}
```

- `server {` - virtual server configuration block
- `location / {` - default location block
- `add_header` - sets specified header
- `Strict-Transport-Security` - only allow HTTPs connections
- `Content-Security-Policy` - enable XSS protection using CSP
- `X-XSS-Protection` - don't load pages with possible XSS attacks
- `X-Frame-Options` - don't allow to include our app into 3rd party apps via iframes
- `X-Content-Type-Options` - enable strict usage of MIME types 
- `Referrer-Policy` - don't pass `Referrer` header to other websites that are being visited from our app 
- `Permissions-Policy` - control which browsers APIs can be used by our app


