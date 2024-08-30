import csv
from datetime import datetime
import os
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import random
import time

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

def calculate_bmi(weight, height):
    return weight / ((height/100) ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def generate_health_tips():
    tips = [
        "Stay hydrated! Drink at least 8 glasses of water daily.",
        "Aim for 30 minutes of moderate exercise 5 days a week.",
        "Incorporate more fruits and vegetables into your diet.",
        "Practice mindfulness or meditation to reduce stress.",
        "Get 7-9 hours of sleep each night for optimal health.",
        "Limit processed foods and added sugars in your diet.",
        "Take short breaks to stretch if you sit for long periods.",
        "Regular health check-ups can catch issues early. Don't skip them!"
    ]
    return random.choice(tips)

def track_medication(name):
    filename = f"{name}_medication.csv"
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Medication", "Dosage", "Frequency", "Start Date"])

    while True:
        print("\n1. Add medication")
        print("2. View medications")
        print("3. Return to main menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            med = input("Enter medication name: ")
            dosage = input("Enter dosage: ")
            freq = input("Enter frequency (e.g., 'twice daily'): ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            with open(filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([med, dosage, freq, start_date])
            print("Medication added successfully!")
        elif choice == '2':
            try:
                with open(filename, 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        print(', '.join(row))
            except FileNotFoundError:
                print("No medication records found.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def fitness_challenge():
    exercises = ["Push-ups", "Squats", "Lunges", "Plank", "Jumping Jacks"]
    challenge = random.choice(exercises)
    print(f"\nYour fitness challenge for today: {challenge}")
    input("Press Enter when you're ready to start...")
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Go!")
    start_time = time.time()
    input("Press Enter when you're done...")
    duration = time.time() - start_time
    print(f"Great job! You completed the {challenge} challenge in {duration:.2f} seconds!")

def generate_report(name, age, bp, glucose, weight, height):
    bmi = calculate_bmi(weight, height)
    bmi_category = get_bmi_category(bmi)
    report = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Name": name,
        "Age": age,
        "Blood Pressure": bp,
        "Glucose": glucose,
        "Weight (kg)": weight,
        "Height (cm)": height,
        "BMI": f"{bmi:.2f}",
        "BMI Category": bmi_category,
        "Condition": "Normal",
        "Recommendation": "Keep up the good work!"
    }
    print(f"Generated Report for {name}:")
    for key, value in report.items():
        print(f"{key}: {value}")
    if bp > 120 or glucose > 140 or bmi < 18.5 or bmi >= 25:
        report["Condition"] = "Needs Attention"
        report["Recommendation"] = "Please consult with your doctor."

    return report
    

def save_report(report):
    filename = f"{report['Name']}_report.csv"
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=report.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(report)

    print(f"Report generated and stored as {filename}.")

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
        dates, bp_values, glucose_values, bmi_values = [], [], [], []
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dates.append(datetime.strptime(row['Date'], "%Y-%m-%d %H:%M:%S"))
                bp_values.append(int(row['Blood Pressure']))
                glucose_values.append(int(row['Glucose']))
                if 'BMI' in row:
                    bmi_values.append(float(row['BMI']))
                elif 'Weight (kg)' in row and 'Height (cm)' in row:
                    weight = float(row['Weight (kg)'])
                    height = float(row['Height (cm)'])
                    bmi = calculate_bmi(weight, height)
                    bmi_values.append(bmi)
                else:
                    bmi_values.append(None)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 18))

        ax1.plot(dates, bp_values, label='Blood Pressure', marker='o')
        ax1.set_title(f"Blood Pressure Trend for {name}")
        ax1.set_xlabel("Date")
        ax1.set_ylabel("Blood Pressure")
        ax1.legend()
        ax1.grid(True)

        ax2.plot(dates, glucose_values, label='Glucose', marker='s', color='g')
        ax2.set_title(f"Glucose Trend for {name}")
        ax2.set_xlabel("Date")
        ax2.set_ylabel("Glucose Level")
        ax2.legend()
        ax2.grid(True)

        if any(bmi is not None for bmi in bmi_values):
            valid_dates = [d for d, bmi in zip(dates, bmi_values) if bmi is not None]
            valid_bmis = [bmi for bmi in bmi_values if bmi is not None]
            ax3.plot(valid_dates, valid_bmis, label='BMI', marker='^', color='r')
            ax3.set_title(f"BMI Trend for {name}")
            ax3.set_xlabel("Date")
            ax3.set_ylabel("BMI")
            ax3.legend()
            ax3.grid(True)
        else:
            ax3.text(0.5, 0.5, "No BMI data available", ha='center', va='center')
            ax3.axis('off')

        plt.tight_layout()
        plt.savefig(f"{name}_health_trends.png")
        print(f"Health trends graph saved as {name}_health_trends.png")
        plt.close()
    except FileNotFoundError:
        print(f"No reports found for {name}.")
    except Exception as e:
        print(f"An error occurred while plotting health trends: {e}")

def calculate_health_score(bp, glucose, bmi):
    bp_score = max(0, 100 - abs(bp - 120))
    glucose_score = max(0, 100 - abs(glucose - 100))
    bmi_score = max(0, 100 - 5 * abs(bmi - 22.5))
    return (bp_score + glucose_score + bmi_score) / 3

def update_report(name):
    filename = f"{name}_report.csv"
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            reports = list(reader)

        if not reports:
            print(f"No existing reports found for {name}.")
            return

        print(f"Found {len(reports)} reports for {name}.")
        for i, report in enumerate(reports):
            print(f"{i+1}. Date: {report['Date']}")

        choice = validate_input("Enter the number of the report to update (0 to cancel): ", 0, len(reports))
        if choice == 0:
            return

        report = reports[choice-1]
        print("\nCurrent report values:")
        for key, value in report.items():
            print(f"{key}: {value}")

        print("\nEnter new values (press Enter to keep current value):")
        age = input(f"Age [{report['Age']}]: ") or report['Age']
        bp = input(f"Blood Pressure [{report['Blood Pressure']}]: ") or report['Blood Pressure']
        glucose = input(f"Glucose [{report['Glucose']}]: ") or report['Glucose']
        weight = input(f"Weight (kg) [{report['Weight (kg)']}]: ") or report['Weight (kg)']
        height = input(f"Height (cm) [{report['Height (cm)']}]: ") or report['Height (cm)']

        new_report = generate_report(name, int(age), int(bp), int(glucose), float(weight), float(height))
        new_report['Date'] = report['Date']  # Keep the original date
        reports[choice-1] = new_report

        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=new_report.keys())
            writer.writeheader()
            writer.writerows(reports)

        print("Report updated successfully!")

    except FileNotFoundError:
        print(f"No reports found for {name}.")

def main():
    while True:
        print("\n===== Health Monitoring System =====")
        print("1. Generate New Report")
        print("2. View Report History")
        print("3. Plot Health Trends")
        print("4. Track Medication")
        print("5. Get Health Tip")
        print("6. Fitness Challenge")
        print("7. Update Existing Report")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            name = input("Enter patient name: ")
            age = validate_input("Enter age: ", 0, 120)
            bp = validate_input("Enter blood pressure: ", 80, 200)
            glucose = validate_input("Enter glucose level: ", 50, 300)
            weight = validate_input("Enter weight (kg): ", 20, 300)
            height = validate_input("Enter height (cm): ", 50, 250)

            report = generate_report(name, age, bp, glucose, weight, height)
            save_report(report)
            bmi = float(report['BMI'])
            health_score = calculate_health_score(bp, glucose, bmi)

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
            name = input("Enter patient name: ")
            track_medication(name)

        elif choice == '5':
            print("\nHere's your health tip for today:")
            print(generate_health_tips())

        elif choice == '6':
            fitness_challenge()

        elif choice == '7':
            name = input("Enter patient name: ")
            update_report(name)

        elif choice == '8':
            print("Thank you for using the Health Monitoring System. Stay healthy!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
