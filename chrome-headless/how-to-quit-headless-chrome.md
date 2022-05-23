# How to quit headless Chrome

```bash
pkill -f "(chrome)?(--headless)"
```

- `pkill -f` - kills all processes that match specified pattern
- `(chrome)?(--headless)` - finds all Chrome headless processes 


