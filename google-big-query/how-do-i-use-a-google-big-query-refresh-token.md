# How do I use a Google Big Query refresh token?
// plain

To use a Google Big Query refresh token, you need to first obtain a refresh token from the Google OAuth 2.0 Playground. Once you have the refresh token, you can use it to obtain an access token.

The following example code block uses the `google-auth-library` package to obtain an access token from a refresh token:
```
import google.auth

# Create credentials object from refresh token
credentials = google.auth.credentials.Credentials(
    None,
    refresh_token=refresh_token
)

# Get access token from credentials
access_token = credentials.token
```

The `refresh_token` parameter should be set to the refresh token obtained from the OAuth 2.0 Playground. After executing the code, the `access_token` variable will contain the access token. This access token can then be used to make authenticated requests to the Big Query API.

## Code explanation

- `google.auth`: This is the module from the `google-auth-library` package which contains the `Credentials` class.
- `Credentials`: This is the class from the `google.auth` module which is used to create a credentials object from a refresh token.
- `refresh_token`: This is the parameter for the `Credentials` class which should be set to the refresh token obtained from the OAuth 2.0 Playground.
- `credentials.token`: This is the method for the `Credentials` class which is used to obtain the access token from the credentials object.

## Helpful links
- [Google OAuth 2.0 Playground](https://developers.google.com/oauthplayground/)
- [google-auth-library](https://pypi.org/project/google-auth/)

onelinerhub: [How do I use a Google Big Query refresh token?](https://onelinerhub.com/google-big-query/how-do-i-use-a-google-big-query-refresh-token)