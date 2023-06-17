# How do I check the version of jQuery I'm using?
// plain

To check the version of jQuery you are using, you can use the `jQuery.fn.jquery` property. This property returns a string containing the version number of jQuery.

## Example code

```
console.log(jQuery.fn.jquery);
```
Example output:
```
3.3.1
```

The code above will output the version of jQuery you are currently using, in this case it is `3.3.1`.

You can also check the version of jQuery by looking at the `<script>` tag in your HTML file. If you are using a CDN to include jQuery, the version number will be included in the URL.

For example:
```
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
```

In this example, `3.3.1` is the version of jQuery being used.

## Helpful links

- [jQuery API Documentation](https://api.jquery.com/)
- [jQuery CDN](https://code.jquery.com/)

onelinerhub: [How do I check the version of jQuery I'm using?](https://onelinerhub.com/jquery/how-do-i-check-the-version-of-jquery-i-m-using)