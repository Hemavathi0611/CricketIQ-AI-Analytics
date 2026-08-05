import pandas as pd

deliveries = pd.read_csv("data/raw/deliveries.csv")

with open("outputs/reports/deliveries_report.txt", "w", encoding="utf-8") as f:

    f.write("="*60 + "\n")
    f.write("DELIVERIES DATASET REPORT\n")
    f.write("="*60 + "\n\n")

    f.write(f"Shape:\n{deliveries.shape}\n\n")

    f.write("Columns:\n")
    f.write(str(deliveries.columns.tolist()))
    f.write("\n\n")

    f.write("Info:\n")
    deliveries.info(buf=f)

    f.write("\n\nMissing Values:\n")
    f.write(str(deliveries.isnull().sum()))

    f.write("\n\nFirst Five Rows:\n")
    f.write(deliveries.head().to_string())

    f.write("\n\nLast Five Rows:\n")
    f.write(deliveries.tail().to_string())

    f.write("\n\nStatistical Summary:\n")
    f.write(deliveries.describe(include="all").to_string())

print("Report saved successfully!")