# Hide points in line chart

```javascript
new Chart('chart', {
  // ...
  data: {
      |{|datasets: [{ data: [1, 2, 3], pointRadius: 0 }]|}|
  }
});
```

- 'chart' - id of ```canvas``` element
- data: \[1, 2, 3\] - example dataset
- pointRadius: 0 - setting radius to zero will hide points
