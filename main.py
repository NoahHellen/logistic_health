import pandas as pd

read_file = pd.read_excel("oasis_longitudinal_demographics.xlsx")

read_file.to_csv("covariates.csv")

new_file = pd.read_excel("Predictions.xlsx")

new_file.to_csv("response.csv")