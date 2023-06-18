# How do I convert a ReactJS web application to a mobile app?
// plain

Converting a ReactJS web application to a mobile app requires the use of a mobile framework such as React Native. React Native is a JavaScript framework that allows you to create native mobile applications for iOS and Android.

To convert a ReactJS web application to a mobile app, you will need to install the React Native CLI and use it to create a new React Native project.

```
$ npm install -g react-native-cli
$ react-native init MyProject
```

Once the project is created, you can start porting over your ReactJS code to the React Native project. This will require rewriting some of the code to fit the React Native framework.

You will need to use components from the React Native library instead of the HTML components from the web application. For example, instead of using the `<div>` tag, you will need to use the `<View>` component.

You will also need to use native APIs instead of web APIs for features such as geolocation and push notifications.

The last step is to build the app for the target platform. You can use the React Native CLI to do this.

```
$ react-native run-ios
$ react-native run-android
```

Once the app is built, you can deploy it to the App Store or Google Play.

## Helpful links
1. [React Native](https://facebook.github.io/react-native/)
2. [Getting Started with React Native](https://facebook.github.io/react-native/docs/getting-started.html)
3. [Building Apps with React Native](https://facebook.github.io/react-native/docs/building-apps.html)

onelinerhub: [How do I convert a ReactJS web application to a mobile app?](https://onelinerhub.com/reactjs/how-do-i-convert-a-reactjs-web-application-to-a-mobile-app)