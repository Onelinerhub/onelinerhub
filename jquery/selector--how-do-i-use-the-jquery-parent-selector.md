# selector

How do I use the jQuery parent selector?
// plain

The jQuery parent selector is used to select the parent element of the specified element. This can be useful when you want to apply a style or action to the parent element of a given element.

## Example code

```
$('#child').parent();
```
## Output example

```
[<div id="parent">…</div>]
```

The code above will select the parent element of the element with the ID of “child”.

If you want to select all the parent elements of a given element, you can use the parents() method.

## Example code

```
$('#child').parents();
```
## Output example

```
[<div id="grandparent">…</div>, <div id="parent">…</div>]
```

The code above will select all the parent elements of the element with the ID of “child”.

You can also use the parent selector to traverse the DOM tree and select specific parent elements.

## Example code

```
$('#child').parents('#grandparent');
```
## Output example

```
[<div id="grandparent">…</div>]
```

The code above will select the parent element with the ID of “grandparent” of the element with the ID of “child”.

You can also use the parent selector to select multiple parent elements.

## Example code

```
$('#child').parents('#grandparent, #parent');
```
## Output example

```
[<div id="grandparent">…</div>, <div id="parent">…</div>]
```

The code above will select both the parent elements with the ID of “grandparent” and “parent” of the element with the ID of “child”.

## Helpful links
- [jQuery Parent Selector Documentation](https://api.jquery.com/parent/)
- [jQuery Parents Selector Documentation](https://api.jquery.com/parents/)

onelinerhub: [selector

How do I use the jQuery parent selector?](https://onelinerhub.com/jquery/selector--how-do-i-use-the-jquery-parent-selector)