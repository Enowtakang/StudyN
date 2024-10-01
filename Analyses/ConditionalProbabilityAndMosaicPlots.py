import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic


# define paths and dataset variables
size = (12, 12)

data_work1 = "data1.csv"
data_work2 = "data2.csv"

root_path_load = "path/"
root_path_save = "path/"

results_work1 = "work1/"
results_work2 = "work2/"

# load data
data = pd.read_csv(root_path_load + data_work2)
df = data.drop(columns=['v0', 'v00'])


# Mosaic Plots


def mosaic_plot(dataset, variable1, variable2):
    plt.figure(figsize=size)
    fig, _ = mosaic(
        dataset, [variable1, variable2],
        title=f'Mosaic Plot of {variable1} and {variable2}')
    plt.savefig(
        root_path_save + results_work2 + f'mosaic_plot_{variable1}_{variable2}.png')
    plt.close()


for var1 in df.columns:
    for var2 in df.columns:
        if var1 != var2:
            mosaic_plot(df, var1, var2)

# Bar Plots of Conditional Probabilities


def conditional_prob_plot(dataset, variable1, variable2):
    crosstab = pd.crosstab(
        dataset[variable1], dataset[variable2], normalize='index')

    plt.figure(figsize=size)

    ax = crosstab.plot(kind='bar', stacked=True)
    ax.set_title(f'Conditional Probability of {variable2} given {variable1}')
    ax.set_ylabel('Probability')
    for container in ax.containers:
        ax.bar_label(container, label_type='center')
    plt.savefig(
        root_path_save + results_work2 + f'conditional_prob_plot_{variable1}_{variable2}.png')
    plt.close()


for var1 in df.columns:
    for var2 in df.columns:
        if var1 != var2:
            conditional_prob_plot(df, var1, var2)
