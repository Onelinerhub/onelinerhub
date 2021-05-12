# Validate email

```javascript
var email = 'test@example.com';
const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
var is_email_valid = re.test(String(email).toLowerCase());
```

- var email - declare test email
- const re - regular expression to check email validity ([source](https://stackoverflow.com/questions/46155/how-to-validate-an-email-address-in-javascript))
- is_email_valid - this variable will contain ```true``` if email is valid
