# How can I use Amazon AWS to host and stream a YouTube video?
// plain

You can use Amazon AWS to host and stream a YouTube video by using the CloudFront service. CloudFront is a content delivery network (CDN) that makes it easy to deliver your content to users with low latency and high transfer speeds.

To do this, first create a CloudFront web distribution and specify the origin as the URL of the YouTube video. Then, create a CloudFront streaming distribution and specify the origin as the URL of the YouTube video.

Once the distributions are created, you can use the following example code to stream the video using the CloudFront URL:

```
<video width="640" height="480" controls>
  <source src="https://<cloudfront_url>/video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
```

This code will display the video in the browser and allow the user to control playback.

## Code explanation

- `<video>`: The HTML element for embedding a video.
- `width` and `height`: The width and height of the video (in pixels).
- `controls`: A boolean attribute that enables the user to control playback.
- `<source>`: The HTML element for specifying the source of the video.
- `src`: The URL of the video.
- `type`: The type of video.

## Helpful links
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
- [HTML Video Tag](https://www.w3schools.com/tags/tag_video.asp)

onelinerhub: [How can I use Amazon AWS to host and stream a YouTube video?](https://onelinerhub.com/amazon-redshift/how-can-i-use-amazon-aws-to-host-and-stream-a-youtube-video)