# How can I use ReactJS to create a world map?
// plain

Using ReactJS, you can create a world map by making use of the [React Simple Maps](https://www.react-simple-maps.io/) library. This library provides an array of features that makes it easy to generate a world map with customizations.

Below is an example code block that shows how to create a world map using React Simple Maps:

```
import {
  ComposableMap,
  Geographies,
  Geography,
  Marker
} from "react-simple-maps"

const Map = () => {
  return (
    <ComposableMap>
      <Geographies geography="world-50m-with-population.json">
        {({ geographies }) =>
          geographies.map(geo => (
            <Geography
              key={geo.rsmKey}
              geography={geo}
              fill="#EAEAEC"
              stroke="#D6D6DA"
            />
          ))
        }
      </Geographies>
      <Marker coordinates={[-122.4194, 37.7749]}>
        <circle r={10} fill="#F00" />
      </Marker>
    </ComposableMap>
  )
}

export default Map
```

The code block above will render a world map with a marker at the coordinates `[-122.4194, 37.7749]`.

## Code explanation


1. `import` statement: imports the necessary components from the React Simple Maps library.
2. `ComposableMap` component: renders a world map.
3. `Geographies` component: renders the geography data from the `world-50m-with-population.json` file.
4. `Geography` component: renders individual geographic features.
5. `Marker` component: renders a marker at the specified coordinates.
6. `circle` component: renders a circle at the marker coordinates.

## Helpful links

- [React Simple Maps](https://www.react-simple-maps.io/)
- [Geographic Data](https://www.naturalearthdata.com/downloads/50m-cultural-vectors/)

onelinerhub: [How can I use ReactJS to create a world map?](https://onelinerhub.com/reactjs/how-can-i-use-reactjs-to-create-a-world-map)