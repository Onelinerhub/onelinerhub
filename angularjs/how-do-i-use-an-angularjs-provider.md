# How do I use an AngularJS provider?
// plain

An AngularJS provider is a special type of service that can be used to configure an application during the configuration phase.

To use an AngularJS provider, you must first define the provider in the `config` block of your AngularJS application, as shown in the following example:

```
angular.module('MyApp', [])
  .config(['MyProviderProvider', function(MyProviderProvider) {
    MyProviderProvider.setMyProperty('value');
  }]);
```

The code above defines a provider named `MyProvider` and sets a property `myProperty` to a value of `value`.

Once the provider has been defined, it can be used in the `run` block of your AngularJS application, as shown in the following example:

```
angular.module('MyApp', [])
  .run(['MyProvider', function(MyProvider) {
    console.log(MyProvider.getMyProperty());
  }]);
```

The code above retrieves the value of `myProperty` from the `MyProvider` provider and logs it to the console. The output of the code above would be `value`.

In summary, to use an AngularJS provider:

1. Define the provider in the `config` block of your AngularJS application.
2. Use the provider in the `run` block of your AngularJS application.

## Helpful links

- [AngularJS Provider Documentation](https://docs.angularjs.org/api/ng/provider)
- [AngularJS Tutorial: Understanding Providers](https://www.sitepoint.com/angularjs-providers/)

onelinerhub: [How do I use an AngularJS provider?](https://onelinerhub.com/angularjs/how-do-i-use-an-angularjs-provider)