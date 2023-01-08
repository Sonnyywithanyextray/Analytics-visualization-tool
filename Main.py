import matplotlib.pyplot as plt
import requests

def visualize_download_sources(api_url, platform):
    # Make request to API to retrieve download data
    response = requests.get(api_url)
    download_data = response.json()

    # Process download data to create pie chart
    if platform == 'ios':
        # iOS data processing code goes here
        labels = download_data.keys()
        sizes = download_data.values()
    elif platform == 'android':
        # Android data processing code goes here
        labels = download_data['sources'].keys()
        sizes = download_data['sources'].values()
    else:
        raise ValueError('Invalid platform specified')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def visualize_daily_usage(api_url, platform):
    # Make request to API to retrieve daily usage data
    response = requests.get(api_url)
    daily_usage = response.json()

    # Process daily usage data
    if platform == 'ios':
        # iOS data processing code goes here
        usage_data = daily_usage
    elif platform == 'android':
        # Android data processing code goes here
        usage_data = daily_usage['usage']
    else:
        raise ValueError('Invalid platform specified')

    # Create line plot
    plt.plot(usage_data)
    plt.xlabel('Day')
    plt.ylabel('Usage (minutes)')
    plt.show()

def visualize_weekly_usage(api_url, platform):
    # Make request to API to retrieve weekly usage data
    response = requests.get(api_url)
    weekly_usage = response.json()

    # Process weekly usage data
    if platform == 'ios':
        # iOS data processing code goes here
        usage_data = weekly_usage
    elif platform == 'android':
        # Android data processing code goes here
        usage_data = weekly_usage['usage']
    else:
        raise ValueError('Invalid platform specified')

    # Create bar plot
    plt.bar(range(len(usage_data)), usage_data.values(), align='center')
    plt.xticks(range(len(usage_data)), list(usage_data.keys()))
    plt.xlabel('Week')
    plt.ylabel('Usage (minutes)')
    plt.show()

def visualize_monthly_usage(api_url, platform):
    # Make request to API to retrieve monthly usage data
    # Make request to API to retrieve monthly usage data
    response = requests.get(api_url)
    monthly_usage = response.json()

    # Process monthly usage data
    if platform == 'ios':
        # iOS data processing code goes here
        usage_data = monthly_usage
    elif platform == 'android':
        # Android data processing code goes here
        usage_data = monthly_usage['usage']
    else:
        raise ValueError('Invalid platform specified')

    # Create bar plot
    plt.bar(range(len(usage_data)), usage_data.values(), align='center')
    plt.xticks(range(len(usage_data)), list(usage_data.keys()))
    plt.xlabel('Month')
    plt.ylabel('Usage (minutes)')
    plt.show()

def visualize_referral_count(api_url, platform):
    # Make request to API to retrieve referral count data
    response = requests.get(api_url)
    referral_count = response.json()

    # Process referral count data
    if platform == 'ios':
        # iOS data processing code goes here
        referral_data = referral_count
    elif platform == 'android':
        # Android data processing code goes here
        referral_data = referral_count['referrals']
    else:
        raise ValueError('Invalid platform specified')

    # Create histogram
    plt.hist(referral_data, bins=10)
    plt.xlabel('Number of referrals')
    plt.ylabel('Number of users')
    plt.show()

