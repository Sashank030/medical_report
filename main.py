import csv
from datetime import datetime
import os
import matplotlib.pyplot as plt
from prettytable import PrettyTable

def validate_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_report(name, age, bp, glucose):
    report = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Name": name,
        "Age": age,
        "Blood Pressure": bp,
        "Glucose": glucose,
        "Condition": "Normal",
        "Recommendation": "Keep up the good work!"
    }

    if bp > 120 or glucose > 140:
        report["Condition"] = "Needs Attention"
        report["Recommendation"] = "Please consult with your doctor."

    filename = f"{name}_report.csv"
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=report.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(report)

    print(f"Report generated and stored as {filename}.")
    return report

def display_report_history(name):
    filename = f"{name}_report.csv"
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            table = PrettyTable()
            table.field_names = reader.fieldnames
            for row in reader:
                table.add_row([row[field] for field in reader.fieldnames])
            print(table)
    except FileNotFoundError:
        print(f"No reports found for {name}.")

def plot_health_trends(name):
    filename = f"{name}_report.csv"
    try:
        dates, bp_values, glucose_values = [], [], []
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dates.append(datetime.strptime(row['Date'], "%Y-%m-%d %H:%M:%S"))
                bp_values.append(int(row['Blood Pressure']))
                glucose_values.append(int(row['Glucose']))

        plt.figure(figsize=(12, 6))
        plt.plot(dates, bp_values, label='Blood Pressure', marker='o')
        plt.plot(dates, glucose_values, label='Glucose', marker='s')
        plt.title(f"Health Trends for {name}")
        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"{name}_health_trends.png")
        print(f"Health trends graph saved as {name}_health_trends.png")
    except FileNotFoundError:
        print(f"No reports found for {name}.")

def calculate_health_score(bp, glucose):
    bp_score = max(0, 100 - abs(bp - 120))
    glucose_score = max(0, 100 - abs(glucose - 100))
    return (bp_score + glucose_score) / 2

def main():
    while True:
        print("\n===== Health Monitoring System =====")
        print("1. Generate New Report")
        print("2. View Report History")
        print("3. Plot Health Trends")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter patient name: ")
            age = validate_input("Enter age: ", 0, 120)
            bp = validate_input("Enter blood pressure: ", 80, 200)
            glucose = validate_input("Enter glucose level: ", 50, 300)

            report = generate_report(name, age, bp, glucose)
            health_score = calculate_health_score(bp, glucose)

            print("\nGenerated Report:")
            for key, value in report.items():
                print(f"{key}: {value}")
            print(f"Health Score: {health_score:.2f}/100")

            if health_score < 60:
                print("Warning: Your health score is low. Please consult a doctor.")
            elif health_score < 80:
                print("Your health score is average. There's room for improvement.")
            else:
                print("Great job! Your health score is excellent.")

        elif choice == '2':
            name = input("Enter patient name: ")
            display_report_history(name)

        elif choice == '3':
            name = input("Enter patient name: ")
            plot_health_trends(name)

        elif choice == '4':
            print("Thank you for using the Health Monitoring System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()