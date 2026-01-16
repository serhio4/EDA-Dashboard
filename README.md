# 🎬 IMDb Top 1000 - EDA Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://eda-dashboard-2ohjadwhphos9gg6obwe7c.streamlit.app/)

This project is an interactive **Exploratory Data Analysis (EDA)** dashboard built with Python and Streamlit. It allows users to analyze the IMDb Top 1000 Movies dataset, visualize trends, and discover correlations between critical acclaim and box office success.

## 🔗 Live Demo
Check out the live application here:
👉 **[Launch App](https://eda-dashboard-2ohjadwhphos9gg6obwe7c.streamlit.app/)**

## 📊 Key Features
* **Interactive Filtering:** Filter movies by Release Year range and Minimum IMDb Rating.
* **Real-time KPIs:** Instantly calculate metrics like Total Movies, Average Rating, and Total Box Office Gross based on filters.
* **Data Visualization:**
    * *Bar Charts:* View the Top 10 movies for the selected criteria.
    * *Scatter Plots:* Analyze the correlation between IMDb Rating and Gross Revenue (using a logarithmic scale for better visibility).
* **Data Export:** Download the filtered dataset as a CSV file for further analysis.
* **Automated Data Cleaning:** The app handles raw data issues (e.g., converting currency strings to numbers, handling missing values) in real-time.

## 🛠️ Tech Stack
* **Python 3.x**
* **Streamlit** (Frontend & Dashboarding)
* **Pandas** (Data Manipulation & Cleaning)
* **Plotly Express** (Interactive Charts)

## 📂 Project Structure
```text
├── app.py               # Main application script
├── imdb_top_1000.csv    # Raw dataset
├── requirements.txt     # Python dependencies for deployment
└── README.md            # Project documentation
