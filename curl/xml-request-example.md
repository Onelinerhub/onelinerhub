# XML request example

```bash
curl -X POST https://reqbin.com/echo/post/xml -H "Content-Type: application/xml" -d "<test><name value="Donald"/></test>"
```

- `-X POST` - send POST request
- `/echo/post/xml` - sample URL to post XML to
- `Content-Type: application/xml` - let curl know that we're sending XML
- `-d` - specify data to send
- `<test><name value="Donald"/></test>` - sample XML to post


