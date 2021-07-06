# Disable hover tooltips

```javascript
new Chart('chart', {
  // ...
  options: { |{|events: []|}| }
});
```

- 'chart' - id of ```canvas``` element
- events: \[\] - disables all standard events for hover (tooltips)
