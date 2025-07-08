import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        data['Date'] = pd.to_datetime(data['Date'])
        return data
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

def detect_outbreak(data, threshold=50):
    data['Outbreak'] = data['ReportedCases'] > threshold
    return data

def generate_alerts(data):
    alerts = []
    for index, row in data.iterrows():
        if row['Outbreak']:
            alert = f"Outbreak detected on {row['Date'].strftime('%Y-%m-%d')}: {row['ReportedCases']} cases. " \
                    "Recommended intervention: Increase testing and contact tracing."
            alerts.append(alert)
    return alerts

def plot_data(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['ReportedCases'], marker='o', label='Reported Cases')
    plt.axhline(y=50, color='r', linestyle='--', label='Outbreak Threshold')
    plt.title('Community Health Outbreak Monitoring')
    plt.xlabel('Date')
    plt.ylabel('Reported Cases')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outbreak_plot.png')
    plt.show()

def main():
    data = load_data(r'C:\Users\megha\OneDrive\Desktop\CommunityHealthSystem\health_data.csv')
    print("Health Data:")
    print(data)

    data = detect_outbreak(data, threshold=50)
    print("\nOutbreak Detection Results:")
    print(data)

    alerts = generate_alerts(data)
    print("\nAlerts:")
    for alert in alerts:
        print(alert)

    plot_data(data)

if __name__ == "__main__":
    main()
    input("Press Enter to exit")