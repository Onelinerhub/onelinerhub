# How do I integrate an Angular Yandex Map into my software development project?
// plain

Integrating an Angular Yandex Map into a software development project is quite straightforward.

First, you need to install the [Yandex Maps Angular](https://github.com/ymaps/angular-yandex-maps) package.

```
npm install --save angular-yandex-maps
```

Then, you need to add the `AngularYandexMapsModule` to the `imports` array of the application module.

```typescript
import { AngularYandexMapsModule } from 'angular-yandex-maps';

@NgModule({
  imports: [
    ...
    AngularYandexMapsModule.forRoot(),
    ...
  ],
  ...
})
export class AppModule { }
```

Next, you need to add the `<ya-map>` element to the template of the component where you want to show the map.

```html
<ya-map [center]="[55.75, 37.57]">
  <ya-marker [geometry]="[55.75, 37.57]"></ya-marker>
</ya-map>
```

Finally, you need to provide the `ymaps` object to the `yaMapsSettings` service.

```typescript
import { YaMapsSettings } from 'angular-yandex-maps';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.scss']
})
export class MapComponent implements OnInit {
  constructor(private yaMapsSettings: YaMapsSettings) {}

  ngOnInit() {
    this.yaMapsSettings.ymaps = ymaps;
  }
}
```

That's it. Now you can use the Angular Yandex Map in your project.

## Helpful links
- [Yandex Maps Angular](https://github.com/ymaps/angular-yandex-maps)
- [Yandex Maps API](https://tech.yandex.com/maps/doc/jsapi/2.1/quick-start/index-docpage/)

onelinerhub: [How do I integrate an Angular Yandex Map into my software development project?](https://onelinerhub.com/angularjs/how-do-i-integrate-an-angular-yandex-map-into-my-software-development-project)