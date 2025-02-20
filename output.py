# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---


# %%
import os

import pandas as pd

from app.utils import load_data
from app.features import calculate_features


# %%
file_path = 'data/data.csv'

df = load_data(file_path)
df.head()

# %%
df_features = df.apply(
    lambda row: calculate_features(
        id=row['id'],
        application_date=row['application_date'],
        contracts=row['contracts']
    ),
    axis=1
)
df_features = pd.DataFrame(df_features.tolist())


# %%
output_cols = [
    'id',
    'tot_claim_cnt_l180d',
    'disb_bank_loan_wo_tbc',
    'day_sinlastloan',
]

df_features = df_features[output_cols]
df_features.head()

# %%
os.makedirs('output', exist_ok=True)
df_features[output_cols].to_csv('output/contract_features.csv', index=False)

# %%
