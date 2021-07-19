# How to listen for button click in popup script

Should be executed in [popup page](https://developer.chrome.com/docs/extensions/mv3/user_interface/#popup).

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

- <button>Click</button> - sample button to assign click event to
- document.querySelector('button') - button selector
- addEventListener - listen for specified event
- click - we want to listen for clicks
- console.log('Hi!') - do something here when button is clicked
