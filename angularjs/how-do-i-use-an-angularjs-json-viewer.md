# How do I use an AngularJS JSON viewer?
// plain

1. To use an AngularJS JSON viewer, you must first install the module by running the following command in the terminal: ```npm install angular-json-viewer```.

2. Once the module is installed, you can then import it into your AngularJS project using the following code: ```import { JsonViewerModule } from 'angular-json-viewer';```

3. You can then add the module to the imports array in your application's NgModule, as shown here:

```
@NgModule({
  imports: [
    JsonViewerModule
  ],
  ...
})
export class AppModule { }
```

4. You can then use the `<json-viewer>` component to display a JSON object in your application. For example:

```
<json-viewer [json]="myJsonObject"></json-viewer>
```

5. This component will display the JSON object in a hierarchical tree-like structure, with expandable nodes.

6. You can also customize the appearance of the viewer by passing in additional parameters to the component, such as `expandLevel`, `show-line-numbers`, and `collapsed`.

7. For more information on how to use the AngularJS JSON viewer, see the [official documentation](https://www.npmjs.com/package/angular-json-viewer).

onelinerhub: [How do I use an AngularJS JSON viewer?](https://onelinerhub.com/angularjs/how-do-i-use-an-angularjs-json-viewer)