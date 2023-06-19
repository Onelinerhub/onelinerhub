# How do I use AngularJS to create a map?
// plain

AngularJS can be used to create a map by using the Google Maps JavaScript API. To get started, you will need to include the Google Maps JavaScript API in your page.

```
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap"
    async defer></script>
```

Once the API is included in the page, you can create a map using the `google.maps.Map` constructor. This constructor requires two parameters: a DOM element to contain the map, and an options object.

```
const map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8
});
```

This example code will create a map with a center point of -34.397, 150.644 and a zoom level of 8.

To add additional features, such as markers, to the map, you can use the `google.maps.Marker` constructor. This constructor requires two parameters: a position object and an options object.

```
const marker = new google.maps.Marker({
    position: { lat: -34.397, lng: 150.644 },
    map: map
});
```

This example code will add a marker to the map at the same center point as the map.

For more information on using the Google Maps JavaScript API with AngularJS, see the [Google Maps JavaScript API Documentation](https://developers.google.com/maps/documentation/javascript/tutorial).

onelinerhub: [How do I use AngularJS to create a map?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-to-create-a-map)