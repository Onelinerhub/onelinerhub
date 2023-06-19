# How can I use AngularJS to localize my application?
// plain

AngularJS provides a built-in localization service called `$locale`. It can be used to localize your application and make it available in multiple languages.

## Example code

```javascript
// set language
$locale.id = 'es-MX';

// get localized string
var localizedString = $locale.DATETIME_FORMATS.SHORTDAY[0];
```
## Output example
 `dom`

The code above sets the language to Spanish (Mexico), and retrieves the localized string for the first day of the week.

The `$locale` service provides access to multiple localization-related properties, such as `DATETIME_FORMATS`, `NUMBER_FORMATS`, `MESSAGES`, etc. All of these properties contain localized strings for various elements, such as numbers, dates, times, etc.

## Code explanation

- `$locale.id` - Sets the language for the application.
- `$locale.DATETIME_FORMATS` - Contains localized strings for dates and times.
- `$locale.NUMBER_FORMATS` - Contains localized strings for numbers.
- `$locale.MESSAGES` - Contains localized strings for messages.

## Helpful links
- [AngularJS $locale Service](https://docs.angularjs.org/api/ng/service/$locale)

onelinerhub: [How can I use AngularJS to localize my application?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-to-localize-my-application)