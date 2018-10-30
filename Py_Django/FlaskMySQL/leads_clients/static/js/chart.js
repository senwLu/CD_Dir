window.onload = function() {
  var options = {
    animationEnabled: true,
    title: {
      text: "Customer and number of new leads"
    },
    data: [
      {
        type: "doughnut",
        innerRadius: "40%",
        showInLegend: true,
        legendText: "{label}",
        indexLabel: "{label}: #percent%",
        dataPoints: []
      }
    ]
  };

  // setting up target to push to
  let targetPush = options.data[0].dataPoints;

  for (var key in data_C) {
    targetPush.push({ label: data_C[key].name, y: data_C[key].count });
  }

  $("#chartContainer").CanvasJSChart(options);
};
