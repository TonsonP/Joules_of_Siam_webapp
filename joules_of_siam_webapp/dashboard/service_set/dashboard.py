import pandas as pd

# Since this projects is small, I decide to keep everything in one service set
def get_data_strech():

    '''
    Basically just reading from csv using pandas and convert it to record format.
    '''

    jos_data_strech_path = "/app/joules_of_siam_webapp/dashboard/Joules_of_Siam_Data - Dataset_Strech.csv"
    df = pd.read_csv(jos_data_strech_path)

    # Convert date to make year format look nicer
    df["Date"] = pd.to_datetime(df["Date"], format='%d-%m-%y', errors='coerce')
    df["Date"] = df["Date"].dt.strftime('%Y-%m-%d') 

    return df

def get_data_consumption():
    '''
    Basically just reading from csv using pandas and convert it to record format.
    '''

    jos_data_electricity_consumption = "/app/joules_of_siam_webapp/dashboard/Joules_of_Siam_Data - Electricity_Consumption_Monthly.csv"
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


    