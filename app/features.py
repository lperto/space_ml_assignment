import json

import pandas as pd


def get_tot_claim_cnt_l180d(application_date: pd.Timestamp, df_contracts: pd.DataFrame):
    if df_contracts.empty:
        return -3

    df_contracts = df_contracts[df_contracts['claim_date'] <= application_date]

    date_180_days_before = application_date - pd.Timedelta(days=180)
    df_contracts = df_contracts[df_contracts['claim_date'] >= date_180_days_before]

    df_contracts = df_contracts[df_contracts['claim_date'].notna()]
    return df_contracts.shape[0]


def get_disb_bank_loan_wo_tbc(application_date: pd.Timestamp, df_contracts: pd.DataFrame):
    if df_contracts.empty:
        return -3

    df_contracts = df_contracts[df_contracts['contract_date'] <= application_date]

    excluded_banks = ['LIZ', 'LOM', 'MKO', 'SUG']
    if 'bank' not in df_contracts.columns:
        return -1
    df_filtered = df_contracts[
        (~df_contracts['bank'].isin(excluded_banks)) &
        (df_contracts['bank'].notna())
    ]

    df_filtered = df_filtered[df_filtered['contract_date'].notna()]

    if df_filtered.empty:
        return -1

    disb_bank_loan_wo_tbc = df_filtered['loan_summa'].sum()

    return disb_bank_loan_wo_tbc


def get_day_sinlastloan(application_date: pd.Timestamp, df_contracts: pd.DataFrame):
    if df_contracts.empty:
        return -3

    df_filtered = df_contracts[
        (df_contracts['summa'].notna()) &
        (df_contracts['contract_date'].notna())
    ]

    if df_filtered.empty:
        return -1

    last_loan_date = df_filtered['contract_date'].max()

    day_sinlastloan = (application_date - last_loan_date).days

    return day_sinlastloan


def calculate_features(id: str, application_date: pd.Timestamp, contracts: str | None = None) -> dict:
    application_date = pd.to_datetime(application_date)
    contracts_date_format = '%d.%m.%Y'

    if pd.notna(contracts):
        contracts_json = json.loads(contracts)
        if isinstance(contracts_json, list):
            df_contracts = pd.DataFrame(contracts_json)
        elif isinstance(contracts_json, dict):
            df_contracts = pd.DataFrame([contracts_json])
        else:
            df_contracts = pd.DataFrame()
    else:
        df_contracts = pd.DataFrame()

    if not df_contracts.empty:
        df_contracts['claim_date'] = pd.to_datetime(df_contracts['claim_date'], format=contracts_date_format)
        df_contracts['contract_date'] = pd.to_datetime(df_contracts['contract_date'], format=contracts_date_format)
        df_contracts['summa'] = pd.to_numeric(df_contracts['summa'], errors='coerce')
        df_contracts['loan_summa'] = pd.to_numeric(df_contracts['loan_summa'], errors='coerce')

    return {
        'id': id,
        'tot_claim_cnt_l180d': get_tot_claim_cnt_l180d(application_date, df_contracts),
        'disb_bank_loan_wo_tbc': get_disb_bank_loan_wo_tbc(application_date, df_contracts),
        'day_sinlastloan': get_day_sinlastloan(application_date, df_contracts),
    }
