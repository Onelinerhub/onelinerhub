# How do I insert an element after another element using jQuery?
// plain

To insert an element after another element using jQuery, you can use the `.after()` method. This method inserts content after the selected element. For example, the following code will insert a new `<p>` element after the `<h1>` element with the text "Hello World!":

```
$("h1").after("<p>Hello World!</p>");
```

## Code explanation


* `$("h1")` - Selects the `<h1>` element.
* `.after("<p>Hello World!</p>")` - Inserts the specified content after the selected element.

## Helpful links

* [jQuery .after() Method](https://www.w3schools.com/jquery/html_after.asp)

onelinerhub: [How do I insert an element after another element using jQuery?](https://onelinerhub.com/jquery/how-do-i-insert-an-element-after-another-element-using-jquery)