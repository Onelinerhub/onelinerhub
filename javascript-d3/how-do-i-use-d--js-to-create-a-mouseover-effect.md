# How do I use d3.js to create a mouseover effect?
// plain

Using D3.js, you can create mouseover effects with a few lines of code. This example code will create a rectangle that changes color when the mouse moves over it:

```
<svg width="100" height="100">
  <rect width="100" height="100" fill="blue" />
</svg>

<script>
  d3.select("rect")
    .on("mouseover", function() {
      d3.select(this).attr("fill", "red");
    });
</script>
```

This code will create a blue rectangle that will turn red when the mouse moves over it. The code is composed of the following parts:

1. The SVG element, which creates the canvas on which the rectangle will be drawn.
2. The rect element, which creates the rectangle itself.
3. The on method, which sets up the mouseover event listener.
4. The d3.select method, which selects the rect element.
5. The attr method, which sets the fill attribute to red when the mouse moves over the rectangle.

For more information on how to use D3.js to create mouseover effects, see the [D3.js documentation](https://github.com/d3/d3/blob/master/API.md#selections-on).

onelinerhub: [How do I use d3.js to create a mouseover effect?](https://onelinerhub.com/javascript-d3/how-do-i-use-d--js-to-create-a-mouseover-effect)