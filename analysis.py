# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("dataset/student_performance.csv")

# Display first five rows
print("First 5 rows:")
print(data.head())

# Display dataset information
print("\nDataset Information:")
print(data.info())

# Display statistical summary
print("\nStatistical Summary:")
print(data.describe())




# Calculate average scores
average_math = data["Math_Score"].mean()
average_science = data["Science_Score"].mean()
average_english = data["English_Score"].mean()

print("\nAverage Scores:")
print("Math:", round(average_math, 2))
print("Science:", round(average_science, 2))
print("English:", round(average_english, 2))


# Calculate average study hours and attendance
average_study_hours = data["Study_Hours"].mean()
average_attendance = data["Attendance"].mean()

print("\nOther Averages:")
print("Average Study Hours:", round(average_study_hours, 2))
print("Average Attendance:", round(average_attendance, 2))


# Find students with highest and lowest Math scores
highest_math = data.loc[data["Math_Score"].idxmax()]
lowest_math = data.loc[data["Math_Score"].idxmin()]

print("\n3. HIGHEST MATHEMATICS SCORE")
print("-" * 35)
print(f"Student ID : {int(highest_math['Student_ID'])}")
print(f"Math Score : {int(highest_math['Math_Score'])}")
print(f"Study Hours: {int(highest_math['Study_Hours'])}")
print(f"Attendance : {int(highest_math['Attendance'])}%")

print("\n4. LOWEST MATHEMATICS SCORE")
print("-" * 35)
print(f"Student ID : {int(lowest_math['Student_ID'])}")
print(f"Math Score : {int(lowest_math['Math_Score'])}")
print(f"Study Hours: {int(lowest_math['Study_Hours'])}")
print(f"Attendance : {int(lowest_math['Attendance'])}%")

print("\n" + "=" * 50)
print("ANALYSIS COMPLETED")
print("=" * 50)

# ==================================================
# 1. BAR CHART
# ==================================================

subjects = ["Math", "Science", "English"]
averages = [average_math, average_science, average_english]

plt.figure(figsize=(8, 5))

bars = plt.bar(subjects, averages)

plt.title("Average Student Scores by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.ylim(0, 100)

# Display the average above each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 1,
        f"{height:.2f}",
        ha="center",
        va="bottom"
    )

plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.tight_layout()

plt.tight_layout()
plt.savefig("charts/average_scores.png")
plt.show()


# ==================================================
# 2. SCATTER PLOT
# ==================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    data["Study_Hours"],
    data["Math_Score"]
)

plt.title("Study Hours vs Math Score")
plt.xlabel("Study Hours")
plt.ylabel("Math Score")

plt.tight_layout()
plt.savefig("charts/study_hours_vs_score.png")
plt.show()



# ==================================================
# 3. HEATMAP
# ==================================================

# Select numerical columns
numeric_data = data[
    [
        "Age",
        "Study_Hours",
        "Attendance",
        "Math_Score",
        "Science_Score",
        "English_Score"
    ]
]

# Calculate correlation
correlation = numeric_data.corr()

# Create heatmap
plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("charts/correlation_heatmap.png")
plt.show()
