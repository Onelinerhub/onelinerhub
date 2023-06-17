# How do I use a jQuery CDN?
// plain

Using a jQuery CDN is a simple way to add jQuery to your project. You can add the CDN to your HTML page by including the following code in the `<head>` element:
```
<script src="https://code.jquery.com/jquery-3.4.1.min.js" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>
```
This code will load the jQuery library from the jQuery CDN.

The code has four parts:

* `script` - This is an HTML tag that tells the browser to load a script.
* `src` - This is an attribute of the `script` tag that specifies the source of the script. In this example, the source is the jQuery CDN.
* `integrity` - This is an attribute of the `script` tag that specifies a cryptographic hash of the code. This is used to verify that the code has not been modified.
* `crossorigin` - This is an attribute of the `script` tag that specifies the origin of the code.

Once the code is included in your HTML page, you can use jQuery as you normally would. For example, you could use jQuery to select an element and change its text:
```
$('#myElement').text('Hello World!');
```

This code will change the text of the element with the id `myElement` to `Hello World!`.

For more information on using a jQuery CDN, see [jQuery's documentation](https://jquery.com/download/).

onelinerhub: [How do I use a jQuery CDN?](https://onelinerhub.com/jquery/how-do-i-use-a-jquery-cdn)