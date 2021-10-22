# Create Charts in React

```javascript
import React from "react";
import { Doughnut } from "react-chartjs-2";

function Chart() {

  const data = {
    labels: ["Python", "Javascript", "Java", "GoLang", "Rust", "Ruby"],
    datasets: [
      {
        label: "# of Votes",
        data: [15, 20, 10, 16, 2, 3],
        backgroundColor: [
          "rgba(255, 99, 132, 1)",
          "rgba(54, 162, 235, 1)",
          "rgba(255, 206, 86, 1)",
          "rgba(75, 192, 192, 1)",
          "rgba(153, 102, 255, 1)",
          "rgba(255, 159, 64, 1)",
        ],
        borderColor: [
          "rgba(255, 99, 132, 0.2)",
          "rgba(54, 162, 235, 0.2)",
          "rgba(255, 206, 86, 0.2)",
          "rgba(75, 192, 192, 0.2)",
          "rgba(153, 102, 255, 0.2)",
          "rgba(255, 159, 64, 0.2)",
        ],
        borderWidth: 1,
      },
    ],
  };
  
  return (
    <>
      <Doughnut data={data} />
    </>
  );
}

export default Chart;
```

- react-chartjs-2 - npm library for creating charts
- data - object containing all the necessary details such as label, datasets, bg color
- Doughnut - chart component which takes in the data as prop
