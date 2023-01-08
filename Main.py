import matplotlib.pyplot as plt

def visualize_download_sources(download_sources):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = download_sources.keys()
    sizes = download_sources.values()
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def visualize_daily_usage(daily_usage):
    # Line plot
    plt.plot(daily_usage)
    plt.xlabel('Day')
    plt.ylabel('Usage (minutes)')
    plt.show()

def visualize_weekly_usage(weekly_usage):
    # Bar plot
    plt.bar(range(len(weekly_usage)), weekly_usage.values(), align='center')
    plt.xticks(range(len(weekly_usage)), list(weekly_usage.keys()))
    plt.xlabel('Week')
    plt.ylabel('Usage (minutes)')
    plt.show()

def visualize_monthly_usage(monthly_usage):
    # Bar plot
    plt.bar(range(len(monthly_usage)), monthly_usage.values(), align='center')
    plt.xticks(range(len(monthly_usage)), list(monthly_usage.keys()))
    plt.xlabel('Month')
    plt.ylabel('Usage (minutes)')
    plt.show()

def visualize_referral_count(referral_count):
    # Histogram
    plt.hist(referral_count, bins=10)
    plt.xlabel('Number of referrals')
    plt.ylabel('Number of users')
    plt.show()
