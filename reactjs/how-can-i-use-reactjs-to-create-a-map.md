# How can I use ReactJS to create a map?
// plain

ReactJS can be used to create a map by using a library such as [React-Leaflet](https://react-leaflet.js.org/). React-Leaflet is a React library that provides bindings for Leaflet which is a JavaScript library for interactive maps.

## Example code

```js
import { Map, TileLayer } from 'react-leaflet';

<Map center={[51.505, -0.09]} zoom={13}>
  <TileLayer
    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
    attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
  />
</Map>
```

This example code will render a map at the center coordinates of [51.505, -0.09] with a zoom level of 13. The map will be rendered using OpenStreetMap tiles.

The code is composed of the following parts:

1. `import { Map, TileLayer } from 'react-leaflet';`: This imports the Map and TileLayer components from the React-Leaflet library.

2. `<Map center={[51.505, -0.09]} zoom={13}>`: This creates a Map component with the center coordinates of [51.505, -0.09] and a zoom level of 13.

3. `<TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors' />`: This creates a TileLayer component which will render the map using OpenStreetMap tiles.

## Helpful links

- [React-Leaflet Documentation](https://react-leaflet.js.org/)
- [Leaflet Documentation](https://leafletjs.com/reference-1.6.0.html)

onelinerhub: [How can I use ReactJS to create a map?](https://onelinerhub.com/reactjs/how-can-i-use-reactjs-to-create-a-map)