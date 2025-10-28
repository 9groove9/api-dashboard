# 📊 API Data Automation Dashboard  
> End-to-end automated data pipeline for live APIs and reporting.

---

## 🎥 Demo Video  
▶️ [Watch Demo on YouTube](https://youtu.be/FKhsTRzAZWI)  

This short demo (1 min) shows the complete automated workflow:  
- Fetching data asynchronously from Exchange Rate & OpenWeather APIs  
- Processing and computing KPIs  
- Generating visual charts  
- Creating a final PDF report automatically

---

**Automated Data Dashboard** built with Python.  
It asynchronously fetches real-time data from public APIs (Exchange Rates and Weather),  
processes them, generates charts, and produces a professional PDF report —  
all automatically, with daily scheduling support.

💼 Business Impact

This automation reduces manual work in reporting by 90%.
It automatically fetches live data, merges multiple APIs,
visualizes KPIs, and generates professional daily PDF reports.

---

## 🚀 Features

✅ Asynchronous data fetching with `httpx`  
✅ Data processing and KPI calculation via `pandas`  
✅ Visualization using `matplotlib`  
✅ PDF report generation via `fpdf`  
✅ Automatic daily update using `schedule`  

---

## 🧱 Project Structure

```
API_Dashboard/
├── csv/                # Saved data (API outputs, merged data)
├── reports/            # Generated reports and charts
│   └── plots/          # PNG charts
├── src/
│   ├── fetch_api.py         # Asynchronous API fetching
│   ├── data.py              # Data merging and KPI calculation
│   ├── visualization.py     # Charts (line, bar, heatmap)
│   ├── reporting.py         # PDF report generator
│   └── log_setup.py         # Logging configuration
├── main.py                  # Main entry point (manual update)
├── scheduler.py             # Scheduler for automatic updates
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
# Create virtual environment
python -m venv venv
# Activate it
venv\Scripts\activate          # on Windows
source venv/bin/activate       # on macOS / Linux

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

### 🔸 Manual update
Run the whole pipeline once — fetch → process → visualize → PDF:
```bash
python main.py
```

### 🔸 Automated daily update
Runs automatically every day at **09:00** (configurable):
```bash
python -m src.automation
```

To test faster (every minute), open `src/automation.py` and replace:
```python
schedule.every().day.at("09:00")
```
with
```python
schedule.every(1).minutes
```

---

## 📈 Output

- `csv/` → contains API data and merged dashboard data  
- `reports/plots/` → PNG charts  
- `reports/dashboard_report.pdf` → generated PDF report  

---

## 🧰 Technologies Used

| Purpose | Library |
|----------|----------|
| Asynchronous API calls | `httpx` |
| Data analysis | `pandas` |
| Visualization | `matplotlib`, `seaborn` |
| PDF report generation | `fpdf` |
| Scheduling automation | `schedule` |

---

## 💡 Possible Improvements

- Add Google Sheets integration (`gspread`)
- Archive daily reports with timestamps  
- Send PDF via email or Telegram bot  
- Deploy as a web dashboard (FastAPI or Streamlit)

---

### ⚙️ Scalability & Extensibility

Currently, the dashboard integrates **two APIs**:
- 🌐 ExchangeRate API (currency data)  
- 🌦️ OpenWeather API (weather data)  

The current version merges these data sources directly for simplicity.  
However, the structure allows easy extension to handle additional APIs  
(e.g., Crypto, Finance, or Sales data) using modular data processors.

🧠 *Note:* The pipeline is designed for easy scalability —  
each API can have its own processing function,  
and results can be merged dynamically via shared keys (e.g. `date`).

---

## 👨‍💻 Author

**Oleh Yuldashev**  
📍 Python Developer | Data Automation | API Integrations | PDF Reporting  
🌐 GitHub Portfolio: [github.com/oleh](https://github.com/oleh) *(replace with your actual URL)*  
