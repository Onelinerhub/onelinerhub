# How to use shared variables with the PCNTL_FORK function in PHP?
// plain

Shared variables can be used with the PCNTL_FORK function in PHP by using the `shmop_open` function. This function creates a shared memory segment and returns a shared memory identifier.

```
<?php
$shm_key = ftok(__FILE__, 't');
$shm_id = shmop_open($shm_key, "c", 0644, 1024);
?>
```

The code above creates a shared memory segment and returns a shared memory identifier.

1. `ftok(__FILE__, 't')`: This function generates a unique key based on the pathname of the current file and a character.
2. `shmop_open($shm_key, "c", 0644, 1024)`: This function creates a shared memory segment and returns a shared memory identifier. The parameters are the key, the access mode, the permissions and the size of the segment.
3. `shmop_write($shm_id, $data, 0)`: This function writes data to the shared memory segment. The parameters are the shared memory identifier, the data to write and the offset.
4. `shmop_read($shm_id, 0, 1024)`: This function reads data from the shared memory segment. The parameters are the shared memory identifier, the offset and the number of bytes to read.

## Helpful links

- [PHP: shmop_open - Manual](https://www.php.net/manual/en/function.shmop-open.php)
- [PHP: shmop_write - Manual](https://www.php.net/manual/en/function.shmop-write.php)
- [PHP: shmop_read - Manual](https://www.php.net/manual/en/function.shmop-read.php)

onelinerhub: [How to use shared variables with the PCNTL_FORK function in PHP?](https://onelinerhub.com/php-pcntl/how-to-use-shared-variables-with-the-pcntl_fork-function-in-php)