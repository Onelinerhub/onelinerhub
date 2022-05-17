# Get Command Line Input Pre-Runtime

```php
$input = getopt('fo:r::', ['flag', 'optional:', 'required::']);
if (array_key_exists('f', $input) || array_key_exists('flag', $input)) {
    echo "Flag found.\n";
}
if (array_key_exists('required', $input) && !empty($input['required'])) {
    echo "Required: " . $input['required'] . "\n";
}
```

- ```$input = getopt``` - assign the options to the variable ``$input``
- ```'f``` - short option for a simple flag called ``f``
- ```o:``` - short option for an optional parameter called ``o`` (defined by ``:``)
- ```r::``` - short option for a required parameter called ``r`` (defined by ``::``)
- ```flag ``` - long option for the ``f`` flag
- ```optional:``` - long option for ``o``, also with optional parameter
- ```required::``` - long option for ``r``, also with required parameter
- ```array_key_exists('f', $input)``` - evaluate if the short option for flag ``f`` exists
- ```array_key_exists('flag', $input)``` - evaluate if the long option for flag ``f`` exists
- ```array_key_exists('required', $input)``` - evaluate if the long option for ``r`` exists
- ```&& !empty($input['required'])``` - evaluate if the long option for ``r`` is also not empty
- ```echo "Required: " . $input['required'] . "\n";``` - output the text given in the required parameter

group: cli_input

## Example: 
```php
# example.php:
$input = getopt('fo:r::', ['flag', 'optional:', 'required::']);
if (array_key_exists('f', $input) || array_key_exists('flag', $input)) {
    echo "Flag found.\n";
}
if (array_key_exists('required', $input) && !empty($input['required'])) {
    echo "Required: " . $input['required'] . "\n";
}
```

php example.php -f --required=test

```
```
Flag found.
Required: test

```

