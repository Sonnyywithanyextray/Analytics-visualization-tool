import matplotlib.pyplot as plt
import requests

def visualize_download_sources(api_url):
    # Make request to API to retrieve download data
    response = requests.get(api_url)
    download_data = response.json()

    # Process download data to create pie chart
    labels = download_data.keys()
    sizes = download_data.values()
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def visualize_daily_usage(api_url):
    # Make request to API to retrieve daily usage data
    response = requests.get(api_url)
    daily_usage = response.json()

    # Create line plot
    plt.plot(daily_usage)
    plt.xlabel('Day')
    plt.ylabel('Usage (minutes)')
    plt.show()

def visualize_weekly_usage(api_url):
    # Make request to API to retrieve weekly usage data
    response = requests.get(api_url)
    weekly_usage = response.json()

    # Create bar plot
    plt.bar(range(len(weekly_usage)), weekly_usage.values(), align='center')
    plt.xticks(range(len(weekly_usage)), list(weekly_usage.keys()))
    plt.xlabel('Week')
    plt.ylabel('Usage (minutes)')
    plt.show()

def visualize_monthly_usage(api_url):
    # Make request to API to retrieve monthly usage data
    response = requests.get(api_url)
    monthly_usage = response.json()

    # Create bar plot
    plt.bar(range(len(monthly_usage)), monthly_usage.values(), align='center')
    plt.xticks(range(len(monthly_usage)), list(monthly_usage.keys()))
    plt.xlabel('Month')
    plt.ylabel('Usage (minutes)')
    plt.show()

def visualize_referral_count(api_url):
    # Make request to API to retrieve referral count data
    response = requests.get(api_url)
    referral_count = response.json()

    # Create histogram
    plt.hist(referral_count, bins=10)
    plt.xlabel('Number of referrals')
    plt.ylabel('Number of users')
    plt.show()
