# How to align a div vertically and horizontally on the page position: absolute

```css
.child-div{
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
}
```

- .child-div - your aligned div
- position: absolute - position your div relatively to its parent 
- left: 50% - position your div halfway to the right
- top: 50% - position your div halfway to the bottom
- transform: translate(-50%, -50%) - position your div halfway to its own origin
