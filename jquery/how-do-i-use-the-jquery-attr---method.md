# How do I use the jQuery attr() method?
// plain

The jQuery `attr()` method is used to get or set attributes and values of selected elements. It can be used to get the value of an attribute for the first element in the set of matched elements or set one or more attributes for every matched element.

Example code block:
```
<script>
  $(document).ready(function(){
    $("button").click(function(){
      var text = $("p").attr("style");
      alert(text);
    });
  });
</script>

<p style="color:red;">This is a paragraph.</p>

<button>Get Attribute</button>
```
## Output example
 `color:red;`

The code above contains the following parts:
- `$("button")`: This is a jQuery selector which selects the button element.
- `.click(function()`: This is a jQuery event handler which attaches a function to the click event of the button element.
- `var text = $("p").attr("style")`: This is a jQuery method which gets the value of the style attribute of the paragraph element.
- `alert(text)`: This is a JavaScript method which displays the value of the variable `text` in an alert box.

## Helpful links
- [jQuery attr() Method](https://www.w3schools.com/jquery/jquery_ref_attributes.asp)
- [jQuery Selectors](https://www.w3schools.com/jquery/jquery_selectors.asp)
- [jQuery Events](https://www.w3schools.com/jquery/jquery_events.asp)

onelinerhub: [How do I use the jQuery attr() method?](https://onelinerhub.com/jquery/how-do-i-use-the-jquery-attr---method)