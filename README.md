# 📉 Amazon Price Tracker  

A Python-based web scraper that tracks Amazon product prices using **BeautifulSoup** and **Requests**. It monitors price changes and sends **email alerts** when the price drops below a specified threshold.  

## 🚀 Features  
✅ Scrapes real-time product prices from Amazon  
✅ Monitors price fluctuations over time  
✅ Sends **email notifications** when the price drops  
✅ Simple and customizable  

## 🛠️ Tech Stack  
- **Python**  
- **BeautifulSoup** (for web scraping)  
- **Requests** (for fetching web pages)  
- **Smtplib** (for sending email alerts)  

## 📌 How It Works  
1. The script extracts product price and details from the given Amazon product URL.  
2. It continuously checks for price updates at scheduled intervals.  
3. If the price falls below the set threshold, it **sends an email alert** to notify the user.  
