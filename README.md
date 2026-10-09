# Student Performance Data Analysis

## Project Overview

This project analyzes student study habits, attendance, and academic performance using Python. It uses Pandas for data analysis, Matplotlib for charts, and Seaborn for correlation visualization.

The objective is to explore patterns in student performance through statistical analysis and data visualization.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

## Dataset

The project uses a synthetic dataset containing 100 student records and 8 columns:

* Student ID
* Gender
* Age
* Study Hours
* Attendance
* Mathematics Score
* Science Score
* English Score

The dataset is created for educational and demonstration purposes and does not contain real student records.

## Data Analysis Performed

* Loaded the CSV dataset using Pandas.
* Displayed the first five records.
* Examined dataset structure and data types.
* Generated descriptive statistics.
* Checked for missing values and duplicate records.
* Calculated average subject scores, study hours, and attendance.
* Identified students with the highest and lowest Mathematics scores.
* Created visualizations to explore score distributions and correlations.

## Visualizations

### 1. Average Student Scores by Subject

The bar chart compares the average Mathematics, Science, and English scores.

**Observation:**

* Mathematics has the highest average score of 72.08.
* English has an average score of 66.80.
* Science has the lowest average score of 65.51.

### 2. Study Hours vs Mathematics Score

The scatter plot explores the relationship between students' study hours and Mathematics scores.

**Observation:**

The dataset shows a moderate positive correlation of approximately 0.63 between study hours and Mathematics scores. Students who study longer generally tend to have higher Mathematics scores, although individual results vary.

### 3. Correlation Heatmap

The heatmap visualizes correlations among age, study hours, attendance, and subject scores.

**Observation:**

* Study Hours and Mathematics Score: 0.63
* Study Hours and Science Score: 0.47
* Mathematics and English Scores: 0.40
* Attendance and Mathematics Score: 0.19

These values indicate that relationships differ across variables. Correlation does not establish causation.

## Key Insights

1. Mathematics has the highest average score among the three subjects.
2. Study hours have a moderate positive correlation with Mathematics scores.
3. Study hours also show a positive correlation with Science scores.
4. Attendance has a relatively weak correlation with Mathematics scores in this dataset.
5. The relationships between variables are not uniformly strong.

## Project Structure

```text
Project_1_Data_Analysis/
├── charts/
│   ├── average_scores.png
│   ├── study_hours_vs_score.png
│   └── correlation_heatmap.png
├── dataset/
│   └── student_performance.csv
├── analysis.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run the Project

1. Install Python.

2. Clone or download the project repository.

3. Install the required libraries:

   `pip install -r requirements.txt`

4. Run the analysis script from the project directory:

   `python analysis.py`

The script displays the analysis results and generates the visualizations in the `charts` directory.

## Conclusion

This project demonstrates how Python can be used for data cleaning, statistical analysis, and visualization. It explores relationships between study habits, attendance, and academic scores through charts and correlation analysis.

The results describe patterns in a synthetic dataset and should not be generalized to all students.
