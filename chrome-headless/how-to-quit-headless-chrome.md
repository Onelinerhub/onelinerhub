# How to quit headless Chrome

### If you're in the same terminal you've launched headless Chrome, just press `Ctrl+C`. If headless Chrome runs in the background:

```bash
pkill -f "(chrome)?(--headless)"
```

- `pkill -f` - kills all processes that match specified pattern
- `(chrome)?(--headless)` - finds all Chrome headless processes 


