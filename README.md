# Macroeconomic Indicator Explorer

A interactive web application that allows users to compare key macroeconomic indicators across 20 major economies from 2000 to 2024.

## 📊 Live Demo

[Click here to try the live app](https://macroeconomic-indicator-explorer-g9zsvxymtljpunwx9uesqv.streamlit.app/)

## 🎯 Problem & Target User

**Problem:** Economics students and global economy enthusiasts need a simple, interactive way to compare macroeconomic indicators across different countries without manually searching through spreadsheets or statistical yearbooks.

**Target User:** Economics students, self-learners, and anyone interested in global economic trends.

## 📈 Features

- **Interactive Charts:** Line charts with hover details
- **Multi-country Comparison:** Select any combination of 20 major economies
- **5 Key Indicators:** GDP Growth, Inflation, Unemployment Rate, Trade Openness, Government Debt
- **Time Range Selection:** Filter data from 2000 to 2024
- **Summary Statistics:** Automatic calculation of mean, min, and max values

## 📊 Indicators Meaning

| Indicator | What it tells you |
|-----------|-------------------|
| GDP Growth (%) | Economic growth rate |
| Inflation (%) | Price level changes (2% is typical target) |
| Unemployment Rate (%) | Labor market slack (4-6% is "full employment") |
| Trade (% of GDP) | Economic openness (higher = more trade-dependent) |
| Government Debt (% of GDP) | Fiscal health (above 90% is considered risky) |

## 🌍 Countries Included

China, United States, Japan, Germany, United Kingdom, France, Italy, Canada, South Korea, Australia, India, Brazil, Mexico, Turkey, Indonesia, Saudi Arabia, South Africa, Argentina, Egypt, Netherlands

## 🛠️ Tech Stack

- **Python** - Core data processing
- **Streamlit** - Interactive web framework
- **Pandas** - Data manipulation and analysis
- **Plotly** - Interactive visualizations
- **wbdata** - World Bank Open Data API

## 📂 Project Structure
├── app.py # Main Streamlit application
├── notebook.ipynb # Data acquisition and analysis notebook
├── macro_data.csv # Processed dataset
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── *.png # Generated charts

text

## 🔧 How to Run Locally

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

1. Clone the repository
```bash
git clone https://github.com/orton11/Macroeconomic-Indicator-Explorer.git
cd Macroeconomic-Indicator-Explorer
Install dependencies

bash
pip install -r requirements.txt
Run the application

bash
streamlit run app.py
Open your browser and navigate to http://localhost:8501

📁 Data Source
Source: World Bank Open Data (World Development Indicators)

Access Date: April 2026

License: Creative Commons Attribution 4.0 (CC BY 4.0)

📌 Key Findings
Finding	Value
Highest average GDP growth	China (8.19%)
Highest average GDP growth (2nd)	India (6.26%)
Most open economy (highest Trade % of GDP)	Netherlands (141.9%)
Highest government debt (risk indicator)	United Kingdom (128.5%)
Highest government debt (2nd)	Egypt (85.8%)
🚀 Limitations & Future Improvements
Limitations
Government debt data has gaps for some countries

World Bank data is updated annually with ~1-year lag

Some indicators may have missing values for certain years

Future Improvements
Add more indicators (education, healthcare, environment)

Implement correlation analysis between indicators

Add export functionality (PDF/CSV download)

Include forecast/prediction models

📝 AI Disclosure
The following AI tools were used in the development of this project:

Tool	Version	Access Date	Purpose
ChatGPT	GPT-4	April 2026	Code structure assistance, debugging, README generation
GitHub Copilot	Latest	April 2026	Code completion and pandas operations
All data analysis logic, economic interpretations, and final code adjustments are my own work.

👤 Author
Student ID: 2469690

Course: ACC102 - Python Data Product

Track: Track 4 - Interactive Data Analysis Tool

Assignment: Mini Assignment (15%)

📅 Submission Date
April 27, 2026

📄 License
This project is for educational purposes as part of the ACC102 course assignment.
