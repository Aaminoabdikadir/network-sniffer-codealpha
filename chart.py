import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# Raadi faylkii ugu dambeeyay ee CSV ah
list_of_files = glob.glob('sniffer_advanced_*.csv')
if not list_of_files:
    list_of_files = glob.glob('sniffer_log_*.csv')

if list_of_files:
    latest_file = max(list_of_files, key=os.path.getctime)
    print(f"[*] Waxaa la falanqaynayaa faylka: {latest_file}")

    # Akhri xogta CSV-ga
    df = pd.read_csv(latest_file)

    # Tiri inta jeer ee protocol kasta uu soo muuqday
    protocol_counts = df['Protocol'].value_counts()

    # Dhis Garaafka (Pie Chart)
    plt.figure(figsize=(7, 7))
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f1c40f']
    protocol_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=colors[:len(protocol_counts)])
    
    plt.title('Distribution of Network Protocols')
    plt.ylabel('')
    
    # Soo muuji garaafka
    print("[*] Garaafku wuu furmayaa...")
    plt.show()
else:
    print("[!] Wax fayl CSV ah oo la helay ma jiro.")