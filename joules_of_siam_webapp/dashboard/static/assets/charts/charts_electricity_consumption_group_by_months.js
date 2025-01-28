var selector = document.getElementById("dataSelector");
var charts_energy_consumption_group_by_month = document.getElementById('energy_consumption_group_by_month').getContext('2d');
var currentChart = null;

function generate_charts_energy_consumption_group_by_month(sector) {
    console.log(sector);

    fetch('/_post_charts_electricity_consumption_group_by_month_graph', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            sector: sector
        }),
    }).then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log(data);

        var values = data.values;
        var maxValue = Math.max(...values);

        // Calculate dynamic background colors
        var backgroundColor = values.map(value => {
            var intensity = Math.round((value / maxValue) * 255);
            return `rgba(${255 - intensity}, ${100 + intensity / 2}, ${intensity}, 0.8)`;
        });

        // Chart data
        var charts_data = {
            labels: data.labels,
            datasets: [{
                data: values,
                backgroundColor: backgroundColor,
                borderColor: 'rgba(0, 0, 0, 0.8)',
                borderWidth: 1
            }]
        };

        // Calculate graph scales
        graph_scales_min = Math.min(...values) - 100;
        graph_scales_max = Math.max(...values) + 100;
        console.log(graph_scales_min);
        console.log(graph_scales_max);

        // Chart configuration (fixed "option" typo to "options")
        var config = {
            type: 'bar',
            data: charts_data,
            options: { // Corrected from "option" to "options"
                responsive: true,
                legend: {
                    display: false // Updated to hide legend as there’s no series name
                },
                tooltip: {
                    enabled: false
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        };

        // Destroy the existing chart if it exists
        if (currentChart) {
            currentChart.destroy();
        }

        // Create a new Chart instance
        currentChart = new Chart(charts_energy_consumption_group_by_month, config);
        currentChart.update();
    }).catch(error => {
        console.error('Error while fetching chart data:', error);
    });
}

// Trigger chart generation on dropdown value change
selector.addEventListener('change', function () {
    var selector_values = selector.value;
    generate_charts_energy_consumption_group_by_month(selector_values);
});

// Generate the initial chart on page load
window.addEventListener('load', function () {
    var selector_values = selector.value;
    generate_charts_energy_consumption_group_by_month(selector_values);
});
