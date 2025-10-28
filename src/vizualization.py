import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

from src.log_setup import logging
logger = logging.getLogger(__name__)


def plot_USDEUR_rates(df):
    os.makedirs('reports/plots', exist_ok=True)

    df['date'] = pd.to_datetime(df['date'])
    plt.figure()
    plt.plot(df['date'], df['USDEUR'], marker='o')
    plt.title('USD/EUR exchange rates for last 30 days')
    plt.xlabel('Dates')
    plt.ylabel('Rates')
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    plt.grid(True, alpha=0.8)

    plt.tight_layout()
    plt.savefig('reports/plots/usdeur_exchange_rate.png')
    plt.close()
    logger.info("USDEUR trend plot created successfully.")

def plot_temp_bar(df):
    os.makedirs('reports/plots', exist_ok=True)

    plt.figure
    sns.barplot(data=df, x='city', y='temp', hue='city', palette='Set2')
    plt.title('Cities temperature')
    plt.xlabel('City')
    plt.ylabel('Temperature')
    plt.tight_layout()
    plt.savefig('reports/plots/cities_temperatures.png')
    plt.close()
    logger.info("Temperature bars plot created successfully.")

def plot_heatmap(df):
    os.makedirs('reports/plots', exist_ok=True)
    
    df = df.drop(columns=['city', 'country', 'temp', 'wind_speed', 'weather'])
    
    plt.figure()
    corr_matrix = df.corr(numeric_only=True)
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Corralation matrix')
    plt.tight_layout()
    plt.savefig('reports/plots/exchange_rates_corralations.png')
    plt.close
    logger.info("Corralation matrix plot created successfully.")