# How do I copy text to the clipboard using AngularJS?
// plain

The easiest way to copy text to the clipboard using AngularJS is to use the ngclipboard directive. This directive allows you to easily copy text to the clipboard with a single click. Here is an example of how to use the ngclipboard directive:

```
<button ng-clipboard data-clipboard-text="Hello World!">
  Copy to clipboard
</button>
```

When the button is clicked, the text "Hello World!" will be copied to the clipboard.

The ngclipboard directive has several options that can be used to customize the behavior of the directive. For example, you can specify an on-success callback function which will be called after the text has been successfully copied to the clipboard.

```
<button ng-clipboard data-clipboard-text="Hello World!" on-success="onSuccess()">
  Copy to clipboard
</button>

<script>
  function onSuccess() {
    alert('Text was successfully copied to the clipboard!');
  }
</script>
```

When the button is clicked, the text "Hello World!" will be copied to the clipboard and the onSuccess() function will be called.

The following are the parts of the code used in the example above:

* `ng-clipboard` - This is the directive that is used to enable copying text to the clipboard.
* `data-clipboard-text` - This attribute is used to specify the text that should be copied to the clipboard.
* `on-success` - This attribute is used to specify a callback function that will be called after the text has been successfully copied to the clipboard.

For more information about the ngclipboard directive, see the [documentation](https://github.com/sachinchoolur/ngclipboard).

onelinerhub: [How do I copy text to the clipboard using AngularJS?](https://onelinerhub.com/angularjs/how-do-i-copy-text-to-the-clipboard-using-angularjs)