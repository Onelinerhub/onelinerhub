# How do I integrate YouTube videos into an Angular application?
// plain

Integrating YouTube videos into an Angular application is relatively easy. First, you need to install the `ngx-youtube-player` package. This package allows you to embed YouTube videos into your application.

```
npm install ngx-youtube-player
```

Then, you need to include the package and its components in your application's module.

```
import { YoutubePlayerModule } from 'ngx-youtube-player';

@NgModule({
  imports: [
    YoutubePlayerModule
  ]
})
```

Once the package is installed, you can use the `<youtube-player>` component to embed a YouTube video.

```
<youtube-player
  [videoId]="'v7vKzt9UqCI'"
  (ready)="savePlayer($event)"
  (change)="onStateChange($event)"
></youtube-player>
```

The `videoId` attribute should be set to the video's ID, and `ready` and `change` are optional event handlers.

## Helpful links
* [ngx-youtube-player](https://www.npmjs.com/package/ngx-youtube-player)
* [YouTube Player API Reference for iframe Embeds](https://developers.google.com/youtube/iframe_api_reference)

onelinerhub: [How do I integrate YouTube videos into an Angular application?](https://onelinerhub.com/angularjs/how-do-i-integrate-youtube-videos-into-an-angular-application)