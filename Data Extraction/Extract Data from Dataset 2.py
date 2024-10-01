import pandas as pd


"""
1. Load data
"""
data_path = "path/to/data/"
raw_data = pd.read_excel(data_path, engine='openpyxl')
raw_data.columns = raw_data.columns.str.strip()


renamed_columns = {
    "0.4a Region / Province": "v00",
    "I.3 Sex of respondent": "v0",
    "VI.1 Have you ever heard about the Nuru plantvillage application?": "v1",
    "VI.2 As part of the WAVE program activities, did you receive a smartphone?": "v2",
    "VI.3a Have you been trained to use the Nuru application?": "v3",
    "VI.4a Do you use the Nuru application in cassava cultivation?": "v4",
    "VI.5 Are you able to use the application to diagnose cassava diseases in the field on your own in a practical way?": "v5",
    "VI.8a Have you conducted a diagnostic of neighboring growers' fields?": "v6", }

region = ["v00"]
sex = ["v0"]
variables = ["v1", "v2", "v3", "v4", "v5", "v6"]


def extract_data():
    raw_data.rename(
        columns=renamed_columns,
        inplace=True)

    """extract selected variables"""
    data = raw_data[region + sex + variables]

    """convert data in 'v6' to lowercase"""
    data['v00'] = data['v00'].str.lower()

    """select only rows which contain selected regions"""
    regions = ['adamaoua', 'centre', 'est', 'sud']
    data = data[data['v00'].isin(regions)]

    """save the data subset"""
    path = "path/to/results/"
    data.to_csv(
        path, index_label=False, index=False)


extract_data()
