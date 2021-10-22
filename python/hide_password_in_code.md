# How to hide password in code

```python
import base64

password = base64.b64encode("password$123".encode("utf-8"))
print(password)

```      

- base64.b64encode() - encode string using the standard Base64 alphabet and return the encoded bytes