# How to send emails with JuliaLang?
// plain

JuliaLang provides a package called `Mail` to send emails. To use it, you need to install the package first:
```julia
using Pkg
Pkg.add("Mail")
```

Then you can use the `send` function to send emails:
```julia
using Mail

Mail.send(from = "sender@example.com",
          to = "receiver@example.com",
          subject = "Hello from JuliaLang",
          text = "This is a test email sent from JuliaLang")
```

The `send` function takes the following parameters:
- `from`: the sender's email address
- `to`: the receiver's email address
- `subject`: the subject of the email
- `text`: the body of the email

For more information, please refer to the [Mail package documentation](https://juliapackages.com/docs/Mail/).

onelinerhub: [How to send emails with JuliaLang?](https://onelinerhub.com/julialang/how-to-send-emails-with-julialang)