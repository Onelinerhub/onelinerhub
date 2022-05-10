# How to listen for button click in popup script

```html
<html>
  <body>
    <button>Click</button>
  </body>
    <script>
      document.querySelector('button').addEventListener('click', function() {
       console.log('Hi!');
      });
  </script>
</html>
```

- `button>Click</button` - sample button to assign click event to
- `document.querySelector('button')` - button selector
- `addEventListener` - listen for specified event
- `'click'` - we want to listen for clicks
- `console.log('Hi!')` - do something here when button is clicked


link_youtube: https://youtu.be/p_kq9OQaUBU
