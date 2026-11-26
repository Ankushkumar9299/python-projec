# Student Attendance & Performance Tracker
**PS No. 47 | Python 3 | Pandas | Matplotlib**

## 1. Project overview
This program reads student attendance and marks from a CSV file. It calculates attendance percentage, identifies students at risk, displays a report, calculates class averages, and creates two charts.

A student is **At Risk** when:
- Attendance is below 75%, OR
- Marks are below 40.

The limits are strict: attendance exactly 75% and marks exactly 40 are treated as OK.

## 2. Folder structure
```text
Student_Attendance_Performance_Tracker/
│
├── main.py
├── requirements.txt
├── README.md
├── data/
│   ├── students.csv
│   └── invalid_test_case.csv
├── docs/
│   ├── Project_Report.pdf
│   ├── Algorithm_and_Flowchart.pdf
│   └── Test_Cases.md
└── output/
    ├── attendance_bar_chart.png
    └── attendance_vs_marks_scatter.png
```

## 3. Requirements
- Python 3
- Pandas
- Matplotlib
- VS Code (recommended)

## 4. How to run in VS Code
1. Extract the ZIP file.
2. Open the extracted folder in VS Code.
3. Open Terminal → New Terminal.
4. Install the required libraries:
   ```bash
   python -m pip install -r requirements.txt
   ```
   If `python` does not work on Windows, try:
   ```bash
   py -m pip install -r requirements.txt
   ```
5. Run:
   ```bash
   python main.py
   ```
   Or on Windows:
   ```bash
   py main.py
   ```

## 5. Menu
- Enter `1` to view the student report.
- Enter `2` to view the summary and charts.
- Enter `3` to exit.

## 6. CSV format
Keep the file at `data/students.csv`. The column names must be exactly:
`Name, Classes_Held, Classes_Attended, Marks`

To test another dataset, replace the rows in `students.csv` but keep the same four column names.

## 7. How the program works
1. Pandas reads the CSV file.
2. The program checks required columns and removes invalid rows.
3. Attendance percentage is calculated:
   `Attendance = (Classes_Attended / Classes_Held) * 100`
4. A student is marked At Risk if attendance is below 75% or marks are below 40.
5. The program displays individual reports or the class summary.
6. Matplotlib creates a bar chart and a scatter chart in the `output` folder.

## 8. Troubleshooting
- **No module named pandas/matplotlib:** run `python -m pip install -r requirements.txt`.
- **CSV not found:** make sure `students.csv` is inside the `data` folder.
- **Charts do not appear:** check that Matplotlib is installed. The chart PNG files are also saved in `output`.
- **Wrong CSV headings:** use the exact headings shown in section 6.
