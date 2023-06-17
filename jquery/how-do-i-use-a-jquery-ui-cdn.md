# How do I use a jQuery UI CDN?
// plain

A jQuery UI CDN (Content Delivery Network) is a way to include jQuery UI in your webpages without having to download and host the library yourself.

To use a jQuery UI CDN, simply add a <script> tag to the <head> of your webpage, with the src attribute set to the URL of the CDN. For example:

```
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js"></script>
```

This will include the jQuery UI library, and you can then use it in your page. For example, you can use it to add a datepicker to an input field:

```
<input type="text" id="datepicker">

<script>
$( "#datepicker" ).datepicker();
</script>
```

The code above will add a basic datepicker to the input field with the ID of "datepicker".

You can find a list of available jQuery UI CDNs [here](https://code.jquery.com/ui/).

For more information on how to use jQuery UI, see the [jQuery UI documentation](https://api.jqueryui.com/).

onelinerhub: [How do I use a jQuery UI CDN?](https://onelinerhub.com/jquery/how-do-i-use-a-jquery-ui-cdn)