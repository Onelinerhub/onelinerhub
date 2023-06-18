# How can I build a Progressive Web App (PWA) with ReactJS?
// plain

To build a Progressive Web App (PWA) with ReactJS, you need to follow these steps:

1. Install the required modules and dependencies:

```
npm install --save react react-dom react-router-dom
```

2. Create a `index.js` file and import the React and ReactDOM modules:

```js
import React from 'react';
import ReactDOM from 'react-dom';
```

3. Create a `App.js` file and add the necessary components:

```js
import React from 'react';

class App extends React.Component {
  render() {
    return (
      <div>
        <h1>My PWA App</h1>
      </div>
    );
  }
}

export default App;
```

4. Add the `<App />` component to the `index.js` file:

```js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
```

5. Create a `manifest.json` file to define the app's metadata:

```json
{
  "name": "My PWA App",
  "short_name": "My PWA App",
  "start_url": "/",
  "display": "standalone"
}
```

6. Create a `service-worker.js` file to enable offline support:

```js
const cacheName = 'my-pwa-app-v1';
const filesToCache = [
  '/',
  '/index.html',
  '/index.js',
  '/manifest.json',
  '/service-worker.js',
];

self.addEventListener('install', function(e) {
  console.log('[ServiceWorker] Install');
  e.waitUntil(
    caches.open(cacheName).then(function(cache) {
      console.log('[ServiceWorker] Caching app shell');
      return cache.addAll(filesToCache);
    })
  );
});
```

7. Finally, register the service worker in the `index.js` file:

```js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));

if ('serviceWorker' in navigator) {
  window.addEventListener('load', function() {
    navigator.serviceWorker.register('/service-worker.js').then(function(registration) {
      // Registration was successful
      console.log('ServiceWorker registration successful with scope: ', registration.scope);
    }, function(err) {
      // registration failed :(
      console.log('ServiceWorker registration failed: ', err);
    });
  });
}
```

With these steps, you can successfully build a Progressive Web App (PWA) with ReactJS.

## Helpful links

- [React Docs](https://reactjs.org/docs/getting-started.html)
- [PWA Docs](https://developers.google.com/web/progressive-web-apps/)

onelinerhub: [How can I build a Progressive Web App (PWA) with ReactJS?](https://onelinerhub.com/reactjs/how-can-i-build-a-progressive-web-app--pwa--with-reactjs)