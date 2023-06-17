# How do I use a jQuery UI Slider?
// plain

jQuery UI Sliders are a great way to allow users to select a value from a range of values. To use a jQuery UI Slider, you must first include the jQuery and jQuery UI libraries in your HTML document.

```
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>
```

Next, you must create a div element in your HTML document to contain the slider.

```
<div id="slider"></div>
```

Then, you must create a JavaScript function to initialize the slider. This function will set the range, orientation, and other options of the slider.

```
$(function() {
  $("#slider").slider({
    range: true,
    min: 0,
    max: 10,
    values: [3, 7],
    slide: function(event, ui) {
      $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
    }
  });
});
```

In this example code, we set the range of the slider to be between 0 and 10, and the initial values to be between 3 and 7. We also set a callback function to update an element with the current range of values selected by the slider.

Finally, we must create a text input element to display the current range of values selected by the slider.

```
<input type="text" id="amount" readonly style="border:0; color:#f6931f; font-weight:bold;">
```

## Output example

```
$3 - $7
```

## Helpful links
- [jQuery UI Slider Documentation](https://api.jqueryui.com/slider/)
- [jQuery UI Slider Tutorial](https://www.codexworld.com/jquery-ui-slider-tutorial/)

onelinerhub: [How do I use a jQuery UI Slider?](https://onelinerhub.com/jquery/how-do-i-use-a-jquery-ui-slider)