var currentChart = null;
function electricity_consumption_prediction_charts(){
    let gdp = document.getElementById("gdp_field").value;
    let population = document.getElementById("population_field").value;
    let cpi = document.getElementById("cpi_growth_field").value;

    let ctx = document.getElementById("energy_consumption_forecasting").getContext("2d");

    fetch('/_prediction_electricity_comsumption_forecasting', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "GDP": gdp,
            "CPI": cpi,
            "POPULATION": population
        }),
    }).then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        // Destroy the existing chart if it exists
        if (currentChart) {
            currentChart.destroy();
        }
        // Combine historical and forecasting data
        let historicalDates = data.historical.Date;
        let historicalPeaks = data.historical.Peak;

        let forecastingDates = data.forecasting.Date;
        let forecastingLSTM = data.forecasting.LSTM;
        let forecastingXGBoost = data.forecasting.XGBoost;
        let forecastingLASSO = data.forecasting.LASSO;
        let forecastingThreshold = data.forecasting["Capacity alert threshold"];
        let forecastingGenerationCapacity = data.forecasting["Generation capacity"];

        // Prepare combined chart data
        let labels = [...historicalDates, ...forecastingDates]; // Merge historical and forecasting dates


        let datasets = [
            {
                label: "Historical Peak",
                data: [...historicalPeaks], // Historical data
                borderColor: "gray",
                borderWidth: 2,
                fill: false
            },
            {
                label: "LSTM Forecasting",
                data: [...historicalPeaks, ...forecastingLSTM],
                borderColor: "blue",
                borderWidth: 2,
                fill: false
            },
            {
                label: "XGBoost Forecasting",
                data: [...historicalPeaks, ...forecastingXGBoost],
                borderColor: "green",
                borderWidth: 2,
                fill: false
            },
            {
                label: "LASSO Forecasting",
                data: [...historicalPeaks, ...forecastingLASSO],
                borderColor: "red",
                borderWidth: 2,
                fill: false
            },
            {
                label: "Capacity Alert Threshold",
                data: [...historicalPeaks, ...forecastingThreshold],
                borderColor: "black",
                borderWidth: 1,
                borderDash: [5, 5],
                fill: false
            },
            {
                label: "Generation Capacity",
                data: [...historicalPeaks, ...forecastingGenerationCapacity],
                borderColor: "purple",
                borderWidth: 1,
                borderDash: [5, 5],
                fill: false
            }
        ];

        // Destroy the existing chart if it exists
        if (currentChart) {
                currentChart.destroy();
            }
        
        currentChart = new Chart(ctx, {
            type: "line",
            data: {
                labels: labels, // Dates (both historical and forecasting)
                datasets: datasets // The datasets for each line
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }})



        currentChart.update();

    }).catch(error => {
        console.error('Error while fetching chart data:', error);
    });

    
}
