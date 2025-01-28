var charts_doughnut_electricity_generation = document.getElementById('Charts_Doughnut_Electricity_Generation').getContext('2d');

var backgroundColor = [
  '#9B59B6', '#34495E', '#16A085', '#F39C12', '#D35400', '#C0392B', '#7F8C8D',
  '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40', '#FFCD56',
  '#8E44AD', '#3498DB', '#1ABC9C', '#2ECC71', '#E67E22', '#E74C3C', '#BDC3C7' 
  
];
var hoverBackgroundColor = [
  '#9B59B6CC', '#34495ECC', '#16A085CC', '#F39C12CC', '#D35400CC', '#C0392BCC', '#7F8C8DCC',
  '#FF6384CC', '#36A2EBCC', '#FFCE56CC', '#4BC0C0CC', '#9966FFCC', '#FF9F40CC', '#FFCD56CC',
  '#8E44ADCC', '#3498DBCC', '#1ABC9CCC', '#2ECC71CC', '#E67E22CC', '#E74C3CCC', '#BDC3C7CC' 
];

fetch('/_get_charts_electricity_generation_graph/')
    .then(response => response.json())
    .then(data => {
      new Chart(charts_doughnut_electricity_generation, {
        type: 'doughnut',
        data: {
          labels: data.labels,
          datasets: [{
            data: data.values,
            backgroundColor: backgroundColor.slice(0, data.labels.length), // Match colors to labels
            hoverBackgroundColor: hoverBackgroundColor.slice(0, data.labels.length) // Match hover colors to labels
          }],

        },
        // Options for the chart
        options: {
          responsive: true,
          plugins: {
            legend: {
              position: 'top', // Place the legend on top
            },
            tooltip: {
              enabled: true // Enable tooltips
            }
          }
        }
      });

    })
    .catch(error => {
        console.error('Error while fetching charts_top_left_graph_area:', error)
    });