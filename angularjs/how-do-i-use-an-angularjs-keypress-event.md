# How do I use an AngularJS keypress event?
// plain

To use an AngularJS keypress event, you must first create a directive that will listen for the keypress event. The code for this directive is as follows:

```
app.directive('keypressEvents',
    function ($document, $rootScope) {
        return {
            restrict: 'A',
            link: function () {
                $document.bind('keypress', function (e) {
                    $rootScope.$broadcast('keypress', e, String.fromCharCode(e.which));
                });
            }
        }
    });
```

This directive will broadcast a keypress event when a key is pressed. The event will contain the keypress event object (e) and the character code of the key pressed (String.fromCharCode(e.which)).

To listen for this keypress event, you must create a controller that will act upon the event, such as the following:

```
app.controller('MyCtrl', function($scope, $rootScope) {
    $rootScope.$on('keypress', function(event, e, key) {
        if (key == 'a') {
            // do something
        }
    });
});
```

This controller will listen for the keypress event and act upon it depending on the key pressed. In this example, when the 'a' key is pressed, an action will be taken.

The parts of this code are:

1. Directive: This is a directive that will listen for the keypress event and broadcast it.
2. Broadcast: This is the broadcast of the keypress event, containing the event object and character code of the key pressed.
3. Controller: This is a controller that will listen for the keypress event and act upon it.

## Helpful links

- [AngularJS Keypress Event Directive Tutorial](https://www.tutorialsteacher.com/angularjs/angularjs-keypress-event)
- [AngularJS Documentation](https://angularjs.org/docs)

onelinerhub: [How do I use an AngularJS keypress event?](https://onelinerhub.com/angularjs/how-do-i-use-an-angularjs-keypress-event)