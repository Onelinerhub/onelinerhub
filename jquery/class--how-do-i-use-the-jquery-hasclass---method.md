# Class

How do I use the jQuery hasClass() method?
// plain

The jQuery `hasClass()` method is used to check if an element has a class or not. It returns a boolean value of `true` or `false`.

## Example code

```
<div class="example">
  <p>This is an example.</p>
</div>

<script>
  $(document).ready(function(){
    if ($("div").hasClass("example")) {
      alert("The div has the class 'example'");
    }
  });
</script>
```
## Output example

```
Alert message: The div has the class 'example'
```

## Code explanation


1. `<div class="example">`: This is the element to which the class is applied.

2. `$(document).ready(function(){`: This ensures that the code is executed after the DOM is loaded.

3. `if ($("div").hasClass("example")) {`: This checks if the div element has the class "example".

4. `alert("The div has the class 'example'");`: If the div has the class "example", this alert message is displayed.

5. `});`: This closes the `$(document).ready()` function.

## Helpful links

- [jQuery hasClass() Documentation](https://api.jquery.com/hasclass/)
- [jQuery Tutorial](https://www.tutorialrepublic.com/jquery-tutorial/)

onelinerhub: [Class

How do I use the jQuery hasClass() method?](https://onelinerhub.com/jquery/class--how-do-i-use-the-jquery-hasclass---method)