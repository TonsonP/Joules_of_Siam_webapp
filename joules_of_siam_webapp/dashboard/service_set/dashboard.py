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

    # # TODO: edit this
    # data = {
    #     "labels": ["January", "February", "March", "April", "May"],
    #     "values": [12, 19, 3, 5, 2]
    # }

    return data

    