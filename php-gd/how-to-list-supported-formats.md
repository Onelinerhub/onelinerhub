# How to list supported formats

### You can see list of supported formats by `gd` using `php -i` command and some `grep` to filter output:

```bash
php -i | grep gd -A 10 | grep Support
```

- `php -i` - prints information on php system settings and enabled modules
- `grep gd -A 10` - will filter everything that contains `gd` and print 10 lines after that
- `grep Support` - will filter everything that contains `Support`

## Example: 
```bash
php -i | grep gd -A 10 | grep Support
```
```
GD Support => enabled
FreeType Support => enabled
GIF Read Support => enabled
GIF Create Support => enabled
JPEG Support => enabled
PNG Support => enabled
```

