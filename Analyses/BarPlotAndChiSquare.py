import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency


# define paths and dataset variables
data_work1 = "data1.csv"
data_work2 = "data2.csv"

root_path_load = "path/"
root_path_save = "path/"

results_work1 = "work1/"
results_work2 = "work2/"

# load data
df = pd.read_csv(root_path_load + data_work2)

# Plot Yes/No distribution by sex for every region
# Task 1: Plot Yes/No distribution by sex for each variable
variables = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6']
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99',
          '#FFD700', '#FF69B4']

for i, var in enumerate(variables):
    plt.figure(figsize=(10, 6))

    # Count occurrences of Yes/No by sex and region
    sns.countplot(data=df, x=var, hue='v0',
                  palette=[colors[i], '#D3D3D3'], alpha=0.7)

    # Annotate counts on the bars
    for p in plt.gca().patches:
        plt.annotate(
            f'{p.get_height()}',
            (p.get_x() + p.get_width() / 2., p.get_height()),
            ha='center', va='bottom')

    plt.title(f'Distribution of {var} by Sex')
    plt.xlabel(var)
    plt.ylabel('Count')
    plt.legend(title='Sex')
    plt.xticks(rotation=0)
    # plt.grid(axis='y')

    # Show plot
    plt.tight_layout()

    plt.savefig(
        root_path_save + results_work2 + f'Distribution of {var} by Sex.jpg')

# Chi-square association test and heatmap
chi2_results = pd.DataFrame(index=variables, columns=variables)

for var1 in variables:
    for var2 in variables:
        if var1 != var2:
            contingency_table = pd.crosstab(df[var1], df[var2])
            chi2, p, _, _ = chi2_contingency(contingency_table)
            chi2_results.loc[var1, var2] = p
        else:
            chi2_results.loc[var1, var2] = 1.0  # Diagonal

chi2_results = chi2_results.astype(float)

plt.figure(figsize=(10, 8))
sns.heatmap(
    chi2_results, annot=True,
    cmap='viridis', cbar_kws={'label': 'p-value'})
plt.title('Chi-square Test Results')
plt.savefig(root_path_save + results_work2 + 'Chi-square Test Results.jpg')

