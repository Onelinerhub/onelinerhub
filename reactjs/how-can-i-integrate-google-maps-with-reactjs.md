# How can I integrate Google Maps with ReactJS?
// plain

Integrating Google Maps with ReactJS is relatively straightforward. To begin, you need to include the Google Maps JavaScript library in your React application:

```
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap"
    async defer></script>
```

This will give you access to the Google Maps API. Next, you need to create a `<div>` element that will contain the map. This can be done like so:

```
<div ref={el => (this.mapContainer = el)} className="mapContainer" />
```

The `ref` attribute allows you to access the `<div>` element from within your React component.

Once the `<div>` has been created, you can use the `componentDidMount()` lifecycle method to initialize the map:

```
componentDidMount() {
    this.map = new window.google.maps.Map(this.mapContainer, {
        center: { lat: this.props.lat, lng: this.props.lng },
        zoom: 8
    });
}
```

The code above creates a new instance of the `google.maps.Map` class and passes in the `<div>` element and the map options (center and zoom level).

Finally, you can use the `componentDidUpdate()` lifecycle method to update the map when the props change:

```
componentDidUpdate(prevProps, prevState) {
    if (prevProps.lat !== this.props.lat || prevProps.lng !== this.props.lng) {
        this.map.panTo({ lat: this.props.lat, lng: this.props.lng });
    }
}
```

This code checks if the props have changed and, if so, updates the map.

## Helpful links
- [Google Maps Documentation](https://developers.google.com/maps/documentation/javascript/tutorial)
- [React Documentation](https://reactjs.org/docs/getting-started.html)

onelinerhub: [How can I integrate Google Maps with ReactJS?](https://onelinerhub.com/reactjs/how-can-i-integrate-google-maps-with-reactjs)