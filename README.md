# 🚗📈 India Vehicle Registration Dashboard

This Streamlit dashboard presents vehicle registration trends across 5 years (2021–2025) using data from the **VAHAN portal**.  
It helps investors analyze category-wise growth of **2-wheelers (2W)**, **3-wheelers (3W)**, and **4-wheelers (4W)**.

---

## 🔧 Features

- 📊 Total registrations by vehicle category (2W, 3W, 4W)
- 📈 Year-over-Year (YoY) growth % by category
- 📅 Data from 2021 to 2025
- 📂 Dropdown filter to select vehicle category
- 📋 Clean UI with summary metrics, graphs, and tables

---

## 📁 Folder Structure
vehicle-dashboard/
├── Book2.xlsx
├── app.py
└── README.md

---

## ▶️ How to Run

1. Install dependencies (only once):

```bash
pip install streamlit pandas matplotlib openpyxl

2. Launch the app:
streamlit run app.py
The app will open in your browser at http://localhost:8501

📊 Data Source
Public data collected from the VAHAN Dashboard

Note: Manufacturer-wise data was not available in raw form and is excluded

🔮 Bonus Insight
"Both 2W and 4W categories grew consistently from 2021 to 2024. However, 2025 saw a steep decline of over 43% for 2W and 39% for 4W, possibly indicating a major market shift, saturation, or policy change — a key trigger point for investors."

🚀 Future Roadmap
 Add manufacturer-wise filtering

 Include QoQ (Quarter-over-Quarter) comparison

 Enable download/export of visual insights