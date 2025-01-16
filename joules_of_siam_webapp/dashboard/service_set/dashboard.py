import pandas as pd

# Since this projects is small, I decide to keep everything in one service set
def generated_data():
    '''
    Basically just reading from csv using pandas and convert it to record format.
    '''

    jos_data_strech_path = "/app/joules_of_siam_webapp/dashboard/Joules_of_Siam_Data - Dataset_Strech.csv"
    df = pd.read_csv(jos_data_strech_path)

    # Convert date to make year format look nicer
    df["Date"] = pd.to_datetime(df["Date"], format='%d-%m-%y', errors='coerce')
    df["Date"] = df["Date"].dt.strftime('%Y-%m-%d') 

    return df.to_dict(orient='records')