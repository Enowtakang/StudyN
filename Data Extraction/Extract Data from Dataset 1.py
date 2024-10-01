import pandas as pd


"""
1. Load data
"""
data_path = "path/to/data/"
raw_data = pd.read_excel(data_path, engine='openpyxl')
raw_data.columns = raw_data.columns.str.strip()

"""
2. Extract Data
"""
renamed_columns = {
    "0.4a Region / Province": "v00",
    "I.3 Sex of respondent": "v0",
    "III.1a In the context of cassava production, are you supervised by an agricultural service?": "v1",
    "III.3 Have you ever heard of the WAVE program (Show a picture of WAVE logo if necessary)?": "v2",
    "III.5a Have you participated in the WAVE cassava disease program activities?": "v3",
    "III.6 Did you receive flyers during the training sessions or any others interaction?": "v4",
    "III.7a Do you use this (ese) flyer (s)?": "v5",
    "III.12 Is the dissemination approach adapted to your needs / realities?": "v6", }

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
