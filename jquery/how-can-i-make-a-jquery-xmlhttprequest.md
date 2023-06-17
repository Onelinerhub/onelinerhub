# How can I make a jQuery XMLHttpRequest?
// plain

A jQuery XMLHttpRequest can be made using the jQuery `$.ajax()` method. The `$.ajax()` method takes an object as an argument, allowing you to specify the type of request, the URL, and any data to be sent along with the request.

## Example code


```js
$.ajax({
  type: 'GET',
  url: '/my/url',
  success: function(data) {
    console.log('Success!');
  }
});
```

## Output example
 `Success!`

The `type` field specifies the type of request, either `GET` or `POST`. The `url` field specifies the URL of the resource to be requested. The `success` field is a function that will be called when the request is successful.

## Helpful links

- [jQuery.ajax()](https://api.jquery.com/jquery.ajax/)
- [Using jQuery's $.ajax() Function](https://www.taniarascia.com/how-to-use-jquery-ajax-method/)

onelinerhub: [How can I make a jQuery XMLHttpRequest?](https://onelinerhub.com/jquery/how-can-i-make-a-jquery-xmlhttprequest)