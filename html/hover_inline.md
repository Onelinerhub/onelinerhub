# How to inline style for a:hover

```html
<a href="/page" onmouseover="this.style.color='red'" onmouseout="this.style.color=''" >Link</a>
```

- <a href="/page" - link tag to style hover
- onmouseover - js handler when mouse is over link
- this.style.color='red' - changes color to red when mouse is over
- onmouseout - js handler when mouse is out of link
- this.style.color='' - reset color back to standard
