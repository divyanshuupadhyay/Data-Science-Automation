# Import the Libraries
import yfinance as yf
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import pymongo

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["stock_data"]
collection = db["icici_bank"]

# Define a function that will fetch and store data
def fetch_and_store_data():
    
    try:
        # Get the current time
        now = datetime.now()
        
        # Define the ticker symbol for ICICI Bank
        ticker = "ICICIBANK.NS"
        
        # Get the historical data from 11:00 AM to 2:15 PM (15-minute intervals)
        start_time = now.replace(hour=11, minute=0, second=0)
        end_time = now.replace(hour=14, minute=15, second=0)
        
        # Fetch the data from Yahoo Finance
        data = yf.download(ticker, start=start_time, end=end_time, interval="15m")
        
        # Store the data in MongoDB
        if not data.empty:
            collection.insert_many(data.to_dict(orient="records"))
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
        
# Create a scheduler and schedule the job to run every 15 minutes
scheduler = BlockingScheduler()
scheduler.add_job(fetch_and_store_data, 'interval', minutes=15)

# Run the code 
try:
    # Start the scheduler
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    print("Scheduler stopped manually.")
