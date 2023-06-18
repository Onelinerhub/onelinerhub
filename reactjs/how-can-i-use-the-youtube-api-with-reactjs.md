# How can I use the YouTube API with ReactJS?
// plain

ReactJS is a popular JavaScript library for building user interfaces. It can be used to create interactive web applications with the YouTube API.

To use the YouTube API with ReactJS, you need to install the `youtube-api-search` package from npm. This package provides an easy way to make API requests to YouTube.

Once the package is installed, you can use the following code to make a request to the YouTube API:

```js
import { search } from "youtube-api-search";

const API_KEY = "YOUR_API_KEY";

search({ key: API_KEY, term: "reactjs" }, (results) => {
  console.log(results);
});
```

This code will make a request to the YouTube API and log the results to the console.

The `search` function takes two arguments: an object containing the API key and the search term, and a callback function to be called when the request is complete. The callback function will be passed the results of the API request.

The results will be an array of objects containing information about the videos that match the search term.

For more information on using the YouTube API with ReactJS, see the [YouTube API Documentation](https://developers.google.com/youtube/v3/getting-started).

onelinerhub: [How can I use the YouTube API with ReactJS?](https://onelinerhub.com/reactjs/how-can-i-use-the-youtube-api-with-reactjs)