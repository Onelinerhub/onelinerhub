# How to use OPcache with WordPress and PHP?
// plain

OPcache is a PHP extension that optimizes PHP code execution by caching precompiled script bytecode in shared memory. This helps to reduce server load and improve the performance of WordPress and PHP applications.

To use OPcache with WordPress and PHP, you need to install and enable the OPcache extension in your php.ini file.

```
; Enable OPcache
zend_extension=opcache.so
opcache.enable=1
```

Once enabled, you can check the status of OPcache by running the following command:

```
php -i | grep opcache
```

## Output example

```
opcache
opcache.blacklist_filename => no value => no value
opcache.consistency_checks => 0 => 0
opcache.dups_fix => Off => Off
opcache.enable => On => On
opcache.enable_cli => Off => Off
opcache.enable_file_override => Off => Off
opcache.error_log => no value => no value
opcache.fast_shutdown => 0 => 0
opcache.file_update_protection => 2 => 2
opcache.force_restart_timeout => 180 => 180
opcache.huge_code_pages => Off => Off
opcache.inherited_hack => On => On
opcache.interned_strings_buffer => 8 => 8
opcache.lockfile_path => /tmp => /tmp
opcache.log_verbosity_level => 1 => 1
opcache.max_accelerated_files => 10000 => 10000
opcache.max_file_size => 0 => 0
opcache.max_wasted_percentage => 5 => 5
opcache.memory_consumption => 128 => 128
opcache.optimization_level => 0x7FFFBFFF => 0x7FFFBFFF
opcache.preferred_memory_model => no value => no value
opcache.protect_memory => 0 => 0
opcache.restrict_api => no value => no value
opcache.revalidate_freq => 2 => 2
opcache.revalidate_path => Off => Off
opcache.save_comments => 1 => 1
opcache.use_cwd => On => On
opcache.validate_timestamps => On => On
opcache.validate_permission => Off => Off
opcache.validate_root => Off => Off
```

Once enabled, you can configure OPcache settings in your php.ini file to optimize the performance of WordPress and PHP applications.

## Helpful links
- [PHP OPcache](https://www.php.net/manual/en/book.opcache.php)
- [WordPress OPcache](https://wordpress.org/support/article/optimization-php-configuration/#php-opcache)

onelinerhub: [How to use OPcache with WordPress and PHP?](https://onelinerhub.com/php-wordpress/how-to-use-opcache-with-wordpress-and-php)