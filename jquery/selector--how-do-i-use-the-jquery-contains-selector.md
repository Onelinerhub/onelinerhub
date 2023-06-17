# selector

How do I use the jQuery contains selector?
// plain

The jQuery `contains` selector is used to select elements that contain a specific string of text. The syntax for the `contains` selector is:

```
$(":contains('text')")
```

The selector will return all elements that contain the specified string of text. Here is an example of the `contains` selector in action:

```
<ul>
  <li>Apples</li>
  <li>Bananas</li>
  <li>Oranges</li>
</ul>

<script>
  $( "li:contains('Bananas')" ).css( "background-color", "yellow" );
</script>

<ul>
  <li>Apples</li>
  <li style="background-color: yellow;">Bananas</li>
  <li>Oranges</li>
</ul>
```

In the above example, the `contains` selector is used to select the `li` element that contains the string "Bananas". Then, the `css()` method is used to set the background color of the selected element to yellow.

The parts of the code are:
- `$( "li:contains('Bananas')" )`: This is the `contains` selector. It is used to select the `li` element that contains the string "Bananas".
- `css( "background-color", "yellow" )`: This is the `css()` method. It is used to set the background color of the selected element to yellow.

For more information on the jQuery `contains` selector, please see the following link: [jQuery contains selector](https://api.jquery.com/contains-selector/).

onelinerhub: [selector

How do I use the jQuery contains selector?](https://onelinerhub.com/jquery/selector--how-do-i-use-the-jquery-contains-selector)