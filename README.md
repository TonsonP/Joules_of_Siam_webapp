### Introduction
This projects aim to demonstrate my basic capability of developing web application using BootStrap5 with Django framework.
Joules of Siam was originally a group assignment during my time at AIT for Business Intelligence Analytics
class. I pick up the data and model that we did during that time and create some simple web application based
on that data.

[Joules of Siam](https://github.com/TonsonP/Joules_of_Siam)

### Installation guide

You can run script provided by me. 
```bash
bash start.sh
```
Alternative approach in case you cannot run via bash, you can run below script line by line.
```sh
# Build the Docker image
docker build -t joules_of_siam_webapp ./docker

# Stop and remove any existing container with the same name
docker rm -f joules_of_siam_webapp 2>/dev/null || true

# Run the Docker container in detached mode with a volume mount
docker run -d --name joules_of_siam_webapp \
  -v $(pwd):/app \
  -p 8000:8000 \
  joules_of_siam_webapp
```
Note: you might need to change CMD command in `./docker/Dockerfile`


Bootstrap templates
https://startbootstrap.com/template/sb-admin

### Sample Webpage
This applications consists of 3 main pages.
- [Dashboard](./fig/page_dashboard.png): This also serve as homepage. It contains visualization for electricity peak consumption and features data used for model training.
- [Charts](./fig/page_charts.png): Contains visualization for electricity generation and consumption.
- [Predictions](./fig/page_predictions.png): Visualization for enery consumption forecasting using various models (LSTM, XGBoost, LASSO). Can input features for my model.

### Datasets
Datasets used in this website come from various sources.
- Bank of Thailand (https://www.bot.or.th/en/statistics.html)
- Electricity Generating Authority of Thailand (https://www.egat.co.th/home/statistics/)
- Energy Policy and Planning Office, Ministry of Energy (https://www.eppo.go.th/index.php/th/energy-information#)
- National Statistical Office (https://www.nso.go.th/nsoweb/nso/statistics_and_indicators)

EPPO and EGAT for data relating to electricity usages/consumption/generating.
BOT for data related to economic such as GDP, CPI.
NSO for miscellaneous data, such as Temperature.



