# effect

How can I create a hover effect in ReactJS?
// plain

Creating a hover effect in ReactJS is quite simple. You can use the `onMouseEnter` and `onMouseLeave` events to trigger a function when the mouse enters or leaves an element. For example, the following code block will show an alert when the mouse enters and leaves the element:

```
<div
  onMouseEnter={() => alert("Mouse entered!")}
  onMouseLeave={() => alert("Mouse left!")}
>
  Hover over me!
</div>
```

The code block consists of the following parts:
1. The `<div>` element, which is the element that the hover effect will be applied to.
2. The `onMouseEnter` and `onMouseLeave` events, which are triggered when the mouse enters and leaves the element, respectively.
3. The `alert()` function, which is triggered when the mouse enters or leaves the element.

When the mouse enters and leaves the element, the following output will be displayed:

```
Mouse entered!
Mouse left!
```

For more information, see the [React documentation](https://reactjs.org/docs/events.html#mouse-events) on mouse events.

onelinerhub: [effect

How can I create a hover effect in ReactJS?](https://onelinerhub.com/reactjs/effect--how-can-i-create-a-hover-effect-in-reactjs)