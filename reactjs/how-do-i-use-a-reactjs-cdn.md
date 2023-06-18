# How do I use a ReactJS CDN?
// plain

Using a ReactJS CDN is a great way to quickly add ReactJS to your project without any additional setup.

To use a ReactJS CDN, first include the following script tag in the `<head>` of your HTML document:
```
<script crossorigin src="https://unpkg.com/react@16/umd/react.production.min.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@16/umd/react-dom.production.min.js"></script>
```

These two script tags will load the React and ReactDOM libraries from the CDN.

Once the libraries are loaded, you can use React components in your HTML document. Here is an example of a simple React component:
```
<div id="root"></div>
<script>
  ReactDOM.render(
    <h1>Hello, world!</h1>,
    document.getElementById('root')
  );
</script>
```

The code above will render the text "Hello, world!" in the `<div>` with the `id="root"`.

You can also use the ReactJS CDN to include the development version of React. To do this, replace the `production.min.js` part of the script tag URLs with `development.js`.

## Helpful links
- [ReactJS CDN](https://reactjs.org/docs/cdn-links.html)
- [ReactDOM API Reference](https://reactjs.org/docs/react-dom.html)

onelinerhub: [How do I use a ReactJS CDN?](https://onelinerhub.com/reactjs/how-do-i-use-a-reactjs-cdn)