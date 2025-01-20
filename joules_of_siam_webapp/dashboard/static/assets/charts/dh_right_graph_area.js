var right_graph_ctx = document.getElementById("dh_right_graph");
console.log("test");
fetch('_get_dashboard_home_right_graph/')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        var dh_right_graph = new Chart(right_graph_ctx, {
            type: 'line',
            data: {
                labels: data.labels,       // List of x-axis labels
                datasets: data.datasets    // List of datasets
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
    .catch(error => console.error('Error fetching or rendering graph:', error));
