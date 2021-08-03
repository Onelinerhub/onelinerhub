# Async app example

```php
go(function () { Co::sleep(1); echo 'A'; });
go(function () { echo 'B'; });
```

- go( - launch callback function in the background
- Co::sleep - use this instead of `sleep` to wait for 1 second in the background
- echo 'A' - this should be outputted after 1 second of execution
- echo 'B' - this will be outputted instantly

## Example
```php
go(function () { Co::sleep(1); echo 'A'; });
go(function () { echo 'B'; });
```
```bash
BA
```
