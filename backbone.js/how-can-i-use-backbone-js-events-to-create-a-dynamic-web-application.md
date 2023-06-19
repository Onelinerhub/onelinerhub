# How can I use Backbone.js events to create a dynamic web application?
// plain

Backbone.js events allow developers to create dynamic web applications by responding to user interactions. For example, the following code snippet uses a Backbone event to update a div's contents when a button is clicked:

```js
$('#button').on('click', function(){
  $('#div').html('Button was clicked!');
});
```

When the button with the id of `button` is clicked, the div with the id of `div` will be updated with the message `Button was clicked!`.

Backbone events can also be used to trigger AJAX requests, allowing for dynamic content to be fetched from the server. For example, the following code snippet uses a Backbone event to trigger an AJAX request when a button is clicked:

```js
$('#button').on('click', function(){
  $.ajax({
    url: '/some/url',
    success: function(data){
      $('#div').html(data);
    }
  });
});
```

When the button with the id of `button` is clicked, an AJAX request will be sent to the URL `/some/url`. If the request is successful, the response data will be inserted into the div with the id of `div`.

## Code explanation


- `$('#button')`: Selects the element with the id of `button`
- `on('click', ...)`: Attaches an event handler to the element that will be triggered when the element is clicked
- `$('#div').html(data)`: Inserts the given data into the element with the id of `div`
- `$.ajax(...)`: Sends an AJAX request to the given URL

## Helpful links
- [Backbone.js Events](http://backbonejs.org/#Events)
- [jQuery on() Method](https://www.w3schools.com/jquery/event_on.asp)
- [jQuery html() Method](https://www.w3schools.com/jquery/html_html.asp)
- [jQuery ajax() Method](https://www.w3schools.com/jquery/ajax_ajax.asp)

onelinerhub: [How can I use Backbone.js events to create a dynamic web application?](https://onelinerhub.com/backbone.js/how-can-i-use-backbone-js-events-to-create-a-dynamic-web-application)