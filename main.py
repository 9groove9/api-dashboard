import asyncio
import time
from datetime import datetime, date, timedelta
import os
import pandas as pd
from dotenv import load_dotenv

from src.fetch_api import fetch_all
from src.data import load_data, merge_data, kpi
from src.vizualization import plot_USDEUR_rates, plot_temp_bar, plot_heatmap
from src.reporting import generate_pdf_report


async def update_dashboard():
    print(f'Updating starts at {datetime.now()}')
    
    load_dotenv()  
    ACCESS_KEY = os.getenv("ACCESS_KEY")
    APPID = os.getenv("APPID")
    if not ACCESS_KEY or not APPID:
        raise ValueError("API keys not found. Please add them to your .env file.")
    
    ACCESS_KEY = '564439f3c43e1bdb8f7389dfdad6cce5'
    APPID = 'aada231bd11baac12b33fef434e1d418'
    end_date = date.today()
    start_date = end_date - timedelta(days=30)

    api_requests = [
        {
            'url': 'https://api.exchangerate.host/timeframe',
            'params': {
                'access_key': ACCESS_KEY,
                'start_date': start_date.isoformat(),
                'end_date': end_date.isoformat(),
                'source': 'USD',
                'currencies': 'EUR,GBP,JPY,UAH'
            }
        },
        {
            'url': 'https://api.exchangerate.host/timeframe',
            'params': {
                'access_key': ACCESS_KEY,
                'start_date': start_date.isoformat(),
                'end_date': end_date.isoformat(),
                'source': 'EUR',
                'currencies': 'USD,GBP,JPY,UAH'
            }
        },
        {
            'url': 'https://api.openweathermap.org/data/2.5/weather',
            'params': {
                'lat': '50.45',
                'lon': '30.52',
                'appid': APPID,
                'units': 'metric'
            }
        },
        {
            'url': 'https://api.openweathermap.org/data/2.5/weather',
            'params': {
                'lat': '49.23',
                'lon': '28.48',
                'appid': APPID,
                'units': 'metric'
            }
        }
    ]


    os.makedirs('csv', exist_ok=True)
    
    print('Fetching data...')
    
    start = time.perf_counter()    
    data = await fetch_all(api_requests)
    
    print(f'{len(data)} API endpoints fetched in {time.perf_counter() - start: .2f} sec')

    
    # Exchange rates API to csv
    exchange_frames = []
    weather_frames = []
    for item in data:
        
        if item['name'] == 'https://api.exchangerate.host/timeframe':
            rates = pd.DataFrame(item['data']['quotes']).T.rename_axis('date').reset_index()
            exchange_frames.append(rates)
        
        else:
            df = pd.json_normalize(item['data'])
            df['weather'] = df['weather'].apply(
                lambda w: w[0]['main'] if isinstance(w, list) and len(w) > 0 else None
            )
            city_weather = df.rename(columns={
                'name': 'city',
                'sys.country': 'country',
                'main.temp': 'temp',
                'wind.speed': 'wind_speed',
            })[['city', 'country', 'temp', 'wind_speed', 'weather']]
            weather_frames.append(city_weather)

    exchange_rates = exchange_frames[0].merge(exchange_frames[1], on='date', how='inner')
    exchange_rates.to_csv('csv/exchange_rates.csv', index=False)

    weather = pd.concat(weather_frames, ignore_index=True)
    weather.to_csv('csv/weather.csv', index=False)

    
    # Calculating KPI
    df_rates = load_data('csv/exchange_rates.csv')
    df_weather = load_data('csv/weather.csv')
    merged = merge_data(df_rates, df_weather)
    kpis = kpi(merged)
    merged.to_csv('csv/dashboard.csv')

  
    # Vizualization
    plot_USDEUR_rates(merged)
    plot_temp_bar(merged)
    plot_heatmap(merged)

    
    # Generate dashboard pdf
    generate_pdf_report(kpis)
    print('Dashboard updated!')


if __name__ == '__main__':
    asyncio.run(update_dashboard())
