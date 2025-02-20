import pandas as pd

from pathlib import Path


def load_data(file_path: str = 'data/data.csv') -> pd.DataFrame:

    try:
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f'Data file not found at: {file_path}')

        df = pd.read_csv(file_path)
        df = preprocess_data(df)
        if df.empty:
            raise pd.errors.EmptyDataError('The data file is empty')

        return df

    except Exception as e:
        raise Exception(f'Error loading data from {file_path}: {str(e)}')


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df['id'] = df['id'].astype(int).astype(str)
    df['application_date'] = pd.to_datetime(df['application_date'], format='mixed')
    df['application_date'] = df['application_date'].dt.tz_localize(None)
    return df
