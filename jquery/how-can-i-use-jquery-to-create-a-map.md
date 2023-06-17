# How can I use jQuery to create a map?
// plain

jQuery can be used to create a map by using the Google Maps API. The code below creates a basic map with a marker on it:

```
<div id="map" style="width:400px;height:400px;background:yellow"></div>

<script>
$(document).ready(function(){
  function initMap() {
    var myLatLng = {lat: -25.363, lng: 131.044};

    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 4,
      center: myLatLng
    });

    var marker = new google.maps.Marker({
      position: myLatLng,
      map: map,
      title: 'Hello World!'
    });
  }
});
</script>
<script async defer
src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap">
</script>
```

This code will produce a map with a marker at the coordinates provided. To use this example, the user must first obtain an API key from Google.

The code consists of several parts:

1. The first part is the div with an id of "map" and a width and height of 400px. This is the element that will contain the map.

2. The second part is the jQuery code that is called when the document is ready. This code creates a new google.maps.Map object and passes in the div element as the first parameter. It also sets the zoom level and center of the map.

3. The third part is the code that creates the marker. This code creates a new google.maps.Marker object and passes in the position and map as parameters.

4. The fourth part is the script tag that loads the Google Maps API. This script tag must include the user's API key as a parameter.

Finally, the code will produce a map with a marker at the coordinates provided.

## Helpful links

- [Google Maps API Documentation](https://developers.google.com/maps/documentation/javascript/tutorial)
- [jQuery API Documentation](http://api.jquery.com/)

onelinerhub: [How can I use jQuery to create a map?](https://onelinerhub.com/jquery/how-can-i-use-jquery-to-create-a-map)