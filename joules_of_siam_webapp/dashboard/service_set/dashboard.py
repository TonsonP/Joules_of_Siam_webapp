import pandas as pd
import pickle

data_path = "/app/joules_of_siam_webapp/dashboard/data/"

# Since this projects is small, I decide to keep everything in one service set
def get_data_strech():

    '''
    Basically just reading from csv using pandas and convert it to record format.
    '''

    jos_data_strech_path = data_path + "Joules_of_Siam_Data - Dataset_Strech.csv"
    df = pd.read_csv(jos_data_strech_path)

    # Convert date to make year format look nicer
    df["Date"] = pd.to_datetime(df["Date"], format='%d-%m-%y', errors='coerce')
    df["Date"] = df["Date"].dt.strftime('%Y-%m-%d') 

    return df

def get_data_consumption():
    '''
    Basically just reading from csv using pandas and convert it to record format.
    '''

    jos_data_electricity_consumption = data_path + "Joules_of_Siam_Data - Electricity_Consumption_Monthly.csv"
    df = pd.read_csv(jos_data_electricity_consumption)

    return df


def generated_data():

    df = get_data_strech()

    return df.to_dict(orient='records')

def generated_graph_dh_left_graph():
    '''
    Generate data for graph
    '''

    df = get_data_strech()

    # As df return date from newest to oldest, we need to reverse it.
    date_historical = df["Date"].astype(str).tolist()
    date_historical.reverse()

    values_historical = df["Peak"].tolist()
    values_historical.reverse()

    data = {
        "labels": date_historical,
        "values": values_historical
    }

    return data

def generated_graph_dh_right_graph():
    '''
    Generate right graph for dashboard home
    '''

    # Converts from 2002-1 -> 2002-01
    df = get_data_consumption()
    df[['Year', 'Month']] = df['Date'].str.split('-', expand=True)
    df['Month'] = df['Month'].str.zfill(2)
    df['Date'] = df['Year'] + '-' + df['Month']
    df = df.drop(columns=['Year', 'Month'])

    # Define a palette of 11 distinct colors
    colors = [
        "rgba(75, 192, 192, 0.2)",  # Teal
        "rgba(153, 102, 255, 0.2)", # Purple
        "rgba(255, 99, 132, 0.2)",  # Red
        "rgba(255, 205, 86, 0.2)",  # Yellow
        "rgba(54, 162, 235, 0.2)",  # Blue
        "rgba(255, 159, 64, 0.2)",  # Orange
        "rgba(201, 203, 207, 0.2)", # Grey
        "rgba(75, 0, 130, 0.2)",    # Indigo
        "rgba(123, 239, 178, 0.2)", # Light Green
        "rgba(244, 67, 54, 0.2)",   # Crimson
        "rgba(0, 150, 136, 0.2)"    # Sea Green
    ]
    border_colors = [
        "rgba(75, 192, 192, 1)",
        "rgba(153, 102, 255, 1)",
        "rgba(255, 99, 132, 1)",
        "rgba(255, 205, 86, 1)",
        "rgba(54, 162, 235, 1)",
        "rgba(255, 159, 64, 1)",
        "rgba(201, 203, 207, 1)",
        "rgba(75, 0, 130, 1)",
        "rgba(123, 239, 178, 1)",
        "rgba(244, 67, 54, 1)",
        "rgba(0, 150, 136, 1)"
    ]

    chart_data = {
        "labels": df["Date"].tolist(),  # x-axis labels
        "datasets": [
            {
                "label": column,
                "data": df[column].tolist(),
                "backgroundColor": colors[i % len(colors)],
                "borderColor": border_colors[i % len(border_colors)],
                "borderWidth": 1,
                "pointRadius": 0.7
            }
            for i, column in enumerate(df.columns) if column != "Date"
        ]
    }

    return chart_data


def get_projects_description():

    description = '''
    Electricity demand forecasting is an important task for energy companies and policy makers in Thailand, as it can inform decisions related to
    capacity planning, resource allocation, and pricing. In recent years, Thailand has experienced significant economic and population growth, which
    has led to an increase in energy consumption.

    Electricity demand forecasting is an important task not just for policy makers and electricity providers but also for busonesses and household, as 
    it impacts energy security as well as cost of living or cost of doing business. We see the need to develop a business intelligence system specificially
    for this task.
    '''

    return description

def get_features_explaination():

    features_explaination = '''
    Date: Basically, Year-Month-Day.
    Population: Population of people in Thailand at a specific time, unit in Million.
    Temperature: Temperature in Celsius at a specific time.
    CPI (Consumer Price Index): A measure that examines the weighted average of prices of a basket of consumer goods and services, used to track inflation over time.
    GDP (Gross Domestic Product): The total market value of all final goods and services produced within a country in a given period, typically measured annually or quarterly.
    Peak: Electricity peak usage, unit in Megawatts. This refers to the highest demand for electricity at a specific time.
    '''

    return features_explaination

def get_data_electricity_generation_by_sector():
    '''
    Load .pkl file and transform data for doughnut graph
    '''

    jos_data_generation_by_sector_path = data_path + "df_consumption_sector_2022.pkl"
    with open(jos_data_generation_by_sector_path, "rb") as file:
        jos_data_generation_by_sector = pickle.load(file)

    labels = jos_data_generation_by_sector.index[2:7].to_list()
    values = jos_data_generation_by_sector[2:7].to_list()

    # Basically change 2022.0 -> 2022
    values[0] = int(values[0])

    # Change 6.5 -> 6
    values[1] = int(values[1])

    # round values
    values[2:7] = [round(i, 2) for i in values[2:7]]

    data = {
        "labels": labels,
        "values": values
    }

    return data

def get_data_electricitiy_generation_by_type():

    '''
    Load .pkl file and transform data for doughnut graph
    '''

    jos_data_generation_by_type_path = data_path + "df_generation_type_2022.pkl"
    with open(jos_data_generation_by_type_path, "rb") as file:
        jos_data_generation_by_type = pickle.load(file)

    labels = jos_data_generation_by_type.index[0:7].to_list()
    values = jos_data_generation_by_type[0:7].to_list()

    # Basically change 2022.0 -> 2022
    values[0] = int(values[0])

    # Change 6.5 -> 6
    values[1] = int(values[1])

    # round values
    values[2:7] = [round(i, 2) for i in values[2:7]]

    data = {
        "labels": labels,
        "values": values
    }

    return data

def get_data_electricity_consumption_per_months(sector):
    '''
    Load .pkl file and transform data for bar chart
    '''

    jos_data_consumption_group_by_month_path = data_path + "df_consumption_month_2022.pkl"

    with open(jos_data_consumption_group_by_month_path, "rb") as file:
        df = pickle.load(file)
        # Remove date index
        df = df.reset_index(drop=True)

    data = {
        "labels": df["Month"].to_list(),
        "values": [round(i, 2) for i in df[sector].to_list()]
    }

    return data
