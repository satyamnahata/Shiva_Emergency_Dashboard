import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Store patient data
patients = []

print("🔴 Welcome to Shiva Emergency Ward Tracker 🔴\n")

while True:
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter gender (Male/Female/Other): ")
    illness = input("Enter illness: ")
    urgency = input("Enter urgency level (Low/Medium/High/Critical): ")
    admitted_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Add patient to list
    patients.append({
        "Name": name,
        "Age": age,
        "Gender": gender.capitalize(),
        "Illness": illness.capitalize(),
        "Urgency": urgency.capitalize(),
        "Admitted At": admitted_at
    })

    another = input("\nAdd another patient? (yes/no): ").strip().lower()
    if another != 'yes':
        break

# Create DataFrame
df = pd.DataFrame(patients)

# Save to CSV
df.to_csv("shiva_emergency.csv", index=False)
print("\n✅ Data saved to 'shiva_emergency.csv'")

# Show the table
print("\n📝 Patient Records:")
print(df)

# Plot 1: Urgency level count
plt.figure(figsize=(6, 4))
df['Urgency'].value_counts().plot(kind='bar', color='firebrick')
plt.title("🧯 Patients by Urgency Level")
plt.xlabel("Urgency Level")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()

# Plot 2: Illness frequency
plt.figure(figsize=(6, 4))
df['Illness'].value_counts().plot(kind='barh', color='skyblue')
plt.title("🤒 Patients by Illness")
plt.xlabel("Number of Patients")
plt.ylabel("Illness")
plt.tight_layout()
plt.show()

# Plot 3: Age distribution
plt.figure(figsize=(6, 4))
plt.hist(df['Age'], bins=5, color='purple', edgecolor='black')
plt.title("👶👴 Patient Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()
