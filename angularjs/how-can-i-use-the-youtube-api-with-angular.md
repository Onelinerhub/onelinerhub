# How can I use the YouTube API with Angular?
// plain

Using the YouTube API with Angular can be done by using the [Angular YouTube Embed](https://www.npmjs.com/package/angular-youtube-embed) library. This library allows you to embed YouTube videos into your Angular application with ease.

To use the library, you'll need to install the package:

```
npm install angular-youtube-embed
```

Then you'll need to import the library into your application:

```
import { YoutubeModule } from 'angular-youtube-embed';

@NgModule({
  imports: [
    YoutubeModule
  ]
})
export class AppModule { }
```

After that, you can use the `<youtube-player>` component in your template to embed the video:

```
<youtube-player
  [videoId]="'M7lc1UVf-VE'"
  (ready)="savePlayer($event)"
  (change)="onStateChange($event)"
></youtube-player>
```

The component takes in the `videoId` of the YouTube video you want to embed. It also has two output events, `ready` and `change`, which allow you to capture the player instance and the state changes of the video.

Finally, you'll need to include the YouTube API script in your `index.html` file:

```
<script src="https://www.youtube.com/iframe_api"></script>
```

For more information, you can check out the [official documentation](https://www.npmjs.com/package/angular-youtube-embed).

onelinerhub: [How can I use the YouTube API with Angular?](https://onelinerhub.com/angularjs/how-can-i-use-the-youtube-api-with-angular)