# How to use shared memory with the PCNTL_FORK function in PHP?
// plain

Shared memory is a memory segment that can be accessed by multiple processes. It can be used with the PCNTL_FORK function in PHP to allow multiple processes to access the same data.

## Example code

```
<?php
$shm_key = ftok(__FILE__, 't');
$shm_id = shm_attach($shm_key, 1024, 0600);

if (pcntl_fork() == 0) {
    // Child process
    $data = shm_get_var($shm_id, 1);
    echo "Child read: $data\n";
    shm_detach($shm_id);
} else {
    // Parent process
    shm_put_var($shm_id, 1, "Hello world");
    pcntl_wait($status);
    shm_remove_var($shm_id, 1);
    shm_detach($shm_id);
}
```

## Output example

```
Child read: Hello world
```

## Code explanation

- `$shm_key = ftok(__FILE__, 't');`: Generates a unique key for the shared memory segment.
- `$shm_id = shm_attach($shm_key, 1024, 0600);`: Attaches the shared memory segment to the current process.
- `if (pcntl_fork() == 0) {`: Creates a child process.
- `$data = shm_get_var($shm_id, 1);`: Gets the value of the shared memory segment.
- `echo "Child read: $data\n";`: Prints the value of the shared memory segment.
- `shm_put_var($shm_id, 1, "Hello world");`: Sets the value of the shared memory segment.
- `pcntl_wait($status);`: Waits for the child process to finish.
- `shm_remove_var($shm_id, 1);`: Removes the shared memory segment.
- `shm_detach($shm_id);`: Detaches the shared memory segment from the current process.

## Helpful links
- [PHP: pcntl_fork - Manual](https://www.php.net/manual/en/function.pcntl-fork.php)
- [PHP: shm_attach - Manual](https://www.php.net/manual/en/function.shm-attach.php)
- [PHP: shm_get_var - Manual](https://www.php.net/manual/en/function.shm-get-var.php)
- [PHP: shm_put_var - Manual](https://www.php.net/manual/en/function.shm-put-var.php)
- [PHP: shm_remove_var - Manual](https://www.php.net/manual/en/function.shm-remove-var.php)
- [PHP: shm_detach - Manual](https://www.php.net/manual/en/function.shm-detach.php)

onelinerhub: [How to use shared memory with the PCNTL_FORK function in PHP?](https://onelinerhub.com/php-pcntl/how-to-use-shared-memory-with-the-pcntl_fork-function-in-php)