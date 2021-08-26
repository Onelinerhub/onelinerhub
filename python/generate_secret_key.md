# How to generate a random secret key in hexadecimal

```python
import secrets 
secrets.token_hex(16)
```

- secrets - this module is used for generating cryptographically strong combination of the random numbers and characters.
- token_hex(16) - it returns a random text string in hexadecimal.

# Example
```python
secrets.token_hex(16)
```
```bash
d690a10cf18d4755126cef879d0627d6
```
