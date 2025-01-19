var left_graph_ctx = document.getElementById("dh_left_graph");

// Fetch data from the Django backend
fetch('_get_dashboard_home_left_graph/')
    .then(response => response.json())
    .then(data => {
        // Create the chart using Chart.js
        var dh_left_graph = new Chart(left_graph_ctx, {
            type: 'line', // Change type to 'line'
            data: {
                labels: data.labels,  // Data for the x-axis
                datasets: [{
                    label: 'Peak usage',  // Dataset label
                    data: data.values,     // Data for the y-axis
                    backgroundColor: 'rgba(114, 75, 192, 0.2)', // Area fill color
                    borderColor: 'rgb(85, 22, 211)',        // Line color
                    borderWidth: 2,                              // Thickness of the line
                    pointBackgroundColor: 'rgba(75, 192, 192, 1)', // Color of the data points
                    pointRadius: 0.7,                              // Radius of the data points
                    fill: true                                   // Fill area under the line
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true // Y-axis starts at zero
                    }
                },
                plugins: {
                    legend: {
                        labels: {
                            font: {
                                family: '-apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
                            },
                            color: '#292b2c'
                        }
                    }
                }
            }
        });
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
