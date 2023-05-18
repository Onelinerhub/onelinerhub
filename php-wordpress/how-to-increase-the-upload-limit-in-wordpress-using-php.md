# How to increase the upload limit in WordPress using PHP?
// plain

The upload limit in WordPress can be increased by editing the `php.ini` file. The following code can be used to increase the upload limit:
```
upload_max_filesize = 64M
post_max_size = 64M
max_execution_time = 300
```

The code above will increase the upload limit to 64MB, the post max size to 64MB, and the maximum execution time to 300 seconds.

## Code explanation

- `upload_max_filesize`: This sets the maximum size of a file that can be uploaded.
- `post_max_size`: This sets the maximum size of a post that can be uploaded.
- `max_execution_time`: This sets the maximum time a script can run before it is terminated.

## Helpful links
- [Increasing the Maximum Upload File Size](https://www.wpbeginner.com/wp-tutorials/how-to-increase-the-maximum-file-upload-size-in-wordpress/)
- [PHP.ini File](https://www.php.net/manual/en/ini.core.php)

onelinerhub: [How to increase the upload limit in WordPress using PHP?](https://onelinerhub.com/php-wordpress/how-to-increase-the-upload-limit-in-wordpress-using-php)