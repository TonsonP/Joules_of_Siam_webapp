var ctx = document.getElementById('testdoughnut').getContext('2d');

  // Data for first doughnut chart
  var doughnutData1 = {
    labels: ['Red', 'Blue', 'Yellow'],
    datasets: [{
      data: [300, 50, 100],
      backgroundColor: ['#FF0000', '#0000FF', '#FFFF00'],
      hoverBackgroundColor: ['#FF6666', '#6666FF', '#FFFF66']
    }]
  };

  // Data for second doughnut chart
  var doughnutData2 = {
    labels: ['Green', 'Purple', 'Orange'],
    datasets: [{
      data: [200, 150, 250],
      backgroundColor: ['#00FF00', '#800080', '#FFA500'],
      hoverBackgroundColor: ['#66FF66', '#9933FF', '#FF9966']
    }]
  };

  // Options for both charts
  var options = {
    cutoutPercentage: 70,  // The percentage of the chart's radius that is cut out of the middle
    rotation: -0.5 * Math.PI,  // Start angle of the first doughnut
    circumference: Math.PI,  // Half the circle
    responsive: true,
    maintainAspectRatio: false
  };

  // Create two doughnut charts on the same canvas
  var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: doughnutData1,  // First doughnut chart data
    options: options
  });

  // Create a second doughnut chart with different data
  var myChart2 = new Chart(ctx, {
    type: 'doughnut',
    data: doughnutData2,  // Second doughnut chart data
    options: options
  });