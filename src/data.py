import os
import pandas as pd

from src.log_setup import logging
logger = logging.getLogger(__name__)


def load_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f'File not found {path}')
    return pd.read_csv(path)

def merge_data(df1, df2, how='cross'):
    return df1.merge(df2, how=how)

def kpi(df):
    logger.info('KPI computed')
    return {
        'total_rows': len(df),
        'avg_USD/EUR_rate': df['USDEUR'].mean().round(2) if 'USDEUR' in df else None,
        'avg_temp': df['temp'].mean().round(2) if 'temp' in df else None
    }