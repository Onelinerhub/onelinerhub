# How can I add a PDF viewer to my AngularJS application?
// plain

To add a PDF viewer to an AngularJS application, you can use the [ng2-pdf-viewer](https://www.npmjs.com/package/ng2-pdf-viewer) library. This library provides an Angular component that wraps the [PDF.js](https://mozilla.github.io/pdf.js/) library.

To install this library, you can use npm:

```
npm install ng2-pdf-viewer
```

Once installed, you can use the `PdfViewerComponent` component in your application. For example, you can add the following code to your template:

```html
<pdf-viewer [src]="pdfSrc"></pdf-viewer>
```

In your component, you can provide the `pdfSrc` property with the path to your PDF file, like this:

```js
export class AppComponent {
  pdfSrc: string = '/assets/sample.pdf';
}
```

The `PdfViewerComponent` also provides a number of [options](https://vadimdez.github.io/ng2-pdf-viewer/api) that you can use to customize the viewer.

## Helpful links

- [ng2-pdf-viewer](https://www.npmjs.com/package/ng2-pdf-viewer)
- [PDF.js](https://mozilla.github.io/pdf.js/)
- [PdfViewerComponent API](https://vadimdez.github.io/ng2-pdf-viewer/api)

onelinerhub: [How can I add a PDF viewer to my AngularJS application?](https://onelinerhub.com/angularjs/how-can-i-add-a-pdf-viewer-to-my-angularjs-application)