# How can I create a jQuery popup?
// plain

Creating a jQuery popup is a simple process. To begin, you'll need to include the jQuery library in your HTML file:

```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
```

Next, create an HTML element that will be used for the popup:

```html
<div id="popup">
  <h1>Popup</h1>
  <p>This is a popup!</p>
</div>
```

Then, add the following CSS to style the popup:

```css
#popup {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 400px;
  background: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}
```

Finally, use jQuery to add the functionality to the popup. Add the following code to the bottom of your HTML file:

```javascript
$(document).ready(function() {
  $('#popup').hide();
  $('#open-popup').click(function() {
    $('#popup').show();
  });
  $('#close-popup').click(function() {
    $('#popup').hide();
  });
});
```

This code will create two buttons, `#open-popup` and `#close-popup`, which can be used to open and close the popup respectively. No output is produced.

Parts of the code:

- `<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>`: This line includes the jQuery library.

- `#popup`: This is the HTML element that will be used for the popup.

- `$(document).ready(function() {...})`: This code will run when the document is ready.

- `$('#popup').hide();`: This line will hide the popup when the page loads.

- `$('#open-popup').click(function() {...})`: This code will run when the `#open-popup` button is clicked, and will show the popup.

- `$('#close-popup').click(function() {...})`: This code will run when the `#close-popup` button is clicked, and will hide the popup.

## Helpful links

- [jQuery Documentation](https://api.jquery.com/)
- [CSS Positioning](https://www.w3schools.com/css/css_positioning.asp)

onelinerhub: [How can I create a jQuery popup?](https://onelinerhub.com/jquery/how-can-i-create-a-jquery-popup)