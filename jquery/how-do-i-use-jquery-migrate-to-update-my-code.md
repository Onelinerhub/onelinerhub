# How do I use jQuery migrate to update my code?
// plain

jQuery Migrate is a library that helps you update your code to support the latest jQuery version. It detects deprecated and removed features in your code and provides warnings so that you can update your code to use the latest jQuery version. Here's an example of how to use jQuery Migrate:

```
<script src="https://code.jquery.com/jquery-3.5.1.js"></script>
<script src="https://code.jquery.com/jquery-migrate-3.3.1.js"></script>
<script>
    console.log( $.fn.jquery );
</script>
```

## Output example

```
3.5.1
```

The example above includes two scripts: the jQuery library and the jQuery Migrate library. The jQuery library is used to provide the latest version of jQuery. The jQuery Migrate library is used to detect deprecated and removed features in the code. When the code is run, the jQuery Migrate library will detect any deprecated and removed features and provide warnings.

The code also includes a console.log command to print out the version of jQuery. In this example, the output is 3.5.1, which indicates that the latest version of jQuery is being used.

## Code explanation

1. <script src="https://code.jquery.com/jquery-3.5.1.js"></script> - This is a script tag that includes the latest version of jQuery.
2. <script src="https://code.jquery.com/jquery-migrate-3.3.1.js"></script> - This is a script tag that includes the jQuery Migrate library.
3. console.log( $.fn.jquery ); - This is a console.log command that prints out the version of jQuery being used.

## Helpful links
- https://jquery.com/download/
- https://github.com/jquery/jquery-migrate/

onelinerhub: [How do I use jQuery migrate to update my code?](https://onelinerhub.com/jquery/how-do-i-use-jquery-migrate-to-update-my-code)