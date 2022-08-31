# How to get GD library version

```bash
php -i | grep "GD Support" -A 2
```

- `php -i` - gets information on PHP and installed libs
- `GD Support` - filter output to show info related to GD only
- ` -A 2` - show next 2 lines together with found line

group: install

## Example: 
```bash
php -i | grep "GD Support" -A 2
```
```
GD Support => enabled
GD headers Version => 2.3.0
GD library Version => 2.3.0
```

