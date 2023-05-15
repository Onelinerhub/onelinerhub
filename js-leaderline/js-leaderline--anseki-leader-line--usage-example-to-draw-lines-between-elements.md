# JS leaderline (anseki/leader-line) usage example to draw lines between elements
// plain

JS leaderline (anseki/leader-line) is a JavaScript library that allows you to draw lines between elements on a web page. Here is an example of how to use it:

```
<script src="https://unpkg.com/leader-line@1.2.4/leader-line.min.js"></script>
<div id="start"></div>
<div id="end"></div>
<script>
  var start = document.getElementById('start');
  var end = document.getElementById('end');
  var leaderLine = new LeaderLine(start, end);
</script>
```

This will draw a line between the two elements with the `id`s `start` and `end`.

## Code explanation


- `<script src="https://unpkg.com/leader-line@1.2.4/leader-line.min.js"></script>`: This line loads the JS leaderline library.
- `<div id="start"></div>` and `<div id="end"></div>`: These lines create two elements with the `id`s `start` and `end`.
- `var start = document.getElementById('start');` and `var end = document.getElementById('end');`: These lines get references to the two elements with the `id`s `start` and `end`.
- `var leaderLine = new LeaderLine(start, end);`: This line creates a new leader line between the two elements.

## Helpful links

- [JS leaderline (anseki/leader-line) documentation](https://anseki.github.io/leader-line/)

onelinerhub: [JS leaderline (anseki/leader-line) usage example to draw lines between elements](https://onelinerhub.com/js-leaderline/js-leaderline--anseki-leader-line--usage-example-to-draw-lines-between-elements)