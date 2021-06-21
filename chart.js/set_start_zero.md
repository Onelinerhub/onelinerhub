# Make chart start from zero value

```javascript
new Chart('chart', {
  // ...
  options: { scales: { y: { min: 0 } } }
});
```

- 'chart' - id of ```canvas``` element with height attribute (```<canvas id="chart" height="100"></canvas>```)
- y: { min: 0 } - override minimum value for ```y``` axis to make it start from zero
