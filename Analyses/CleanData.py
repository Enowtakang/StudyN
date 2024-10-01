import pandas as pd


"""
Load Data
"""
path_data = "path/to/data/"

"""
Clean Data
"""


def clean_data(data_path):
    # load dataset
    data = pd.read_csv(data_path)
    # remove all rows with missing values
    data.dropna(inplace=True)
    # remove all spaces between characters in all entries
    region = ["v00"]
    sex = ["v0"]
    variables = ["v1", "v2", "v3", "v4", "v5", "v6"]

    all_variables = region + sex + variables

    for variable in all_variables:
        data[variable] = data[variable].str.replace(' ', '')
        data[variable] = data[variable].str.replace('  ', '')

    # save dataset
    path = "path/to/results/"
    data.to_csv(path, index=False, index_label=False)


clean_data(path_data)
