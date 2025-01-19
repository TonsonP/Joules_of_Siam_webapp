var right_graph_ctx = document.getElementById("myBarChart");

// Fetch data from the Django backend
fetch('_get_dashboard_home_left_graph/')
    .then(response => response.json())
    .then(data => {
        // Create the chart using Chart.js
        var myBarChart = new Chart(right_graph_ctx, {
            type: 'bar',
            data: {
                labels: data.labels,  // Data for the x-axis
                datasets: [{
                    label: 'Sample Data',  // Dataset label
                    data: data.values,     // Data for the y-axis
                    backgroundColor: 'rgba(100, 100, 100, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
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
