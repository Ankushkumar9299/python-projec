"""
Student Attendance & Performance Tracker
PS No.: 47

CSV columns: Name, Classes_Held, Classes_Attended, Marks
A student is At Risk if attendance is below 75% OR marks are below 40.
"""

import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "student.csv"
ATTENDANCE_LIMIT = 75
MARKS_LIMIT = 40


def load_and_clean_data(filename):
    """Load the CSV and remove invalid records."""
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Error: '{filename}' was not found.")
        print("Keep student.csv in the same folder as this Python file.")
        return pd.DataFrame()
    except Exception as error:
        print(f"Error while reading CSV: {error}")
        return pd.DataFrame()

    required_columns = ["Name", "Classes_Held", "Classes_Attended", "Marks"]
    missing = [column for column in required_columns if column not in df.columns]

    if missing:
        print("Invalid CSV. Missing column(s): " + ", ".join(missing))
        print("Required columns: " + ", ".join(required_columns))
        return pd.DataFrame()

    df = df[required_columns].copy()

    # Convert numeric columns. Invalid text such as 'abc' becomes NaN.
    numeric_columns = ["Classes_Held", "Classes_Attended", "Marks"]
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # Remove blank names, missing/non-numeric values and impossible values.
    valid = (
        df["Name"].notna()
        & df["Name"].astype(str).str.strip().ne("")
        & df["Classes_Held"].notna()
        & df["Classes_Attended"].notna()
        & df["Marks"].notna()
        & (df["Classes_Held"] > 0)
        & (df["Classes_Attended"] >= 0)
        & (df["Classes_Attended"] <= df["Classes_Held"])
        & (df["Marks"] >= 0)
        & (df["Marks"] <= 100)
    )

    invalid_count = int((~valid).sum())
    if invalid_count:
        print(f"\n{invalid_count} invalid row(s) skipped.")

    df = df.loc[valid].copy()
    df["Name"] = df["Name"].astype(str).str.strip()

    if df.empty:
        return df

    df["Attendance_Percentage"] = (
        df["Classes_Attended"] / df["Classes_Held"] * 100
    ).round(2)

    # At Risk means strictly below either threshold.
    df["Status"] = (
        (df["Attendance_Percentage"] < ATTENDANCE_LIMIT)
        | (df["Marks"] < MARKS_LIMIT)
    ).map({True: "At Risk", False: "OK"})

    return df


def display_report(df):
    """Display each student's attendance, marks and status."""
    print("\n========== STUDENT REPORT ==========")
    report = df[
        ["Name", "Attendance_Percentage", "Marks", "Status"]
    ].rename(columns={
        "Attendance_Percentage": "Attendance (%)"
    })
    print(report.to_string(index=False))


def display_summary_and_charts(df):
    """Print summary statistics and display bar and scatter charts."""
    average_attendance = df["Attendance_Percentage"].mean()
    average_marks = df["Marks"].mean()
    at_risk = df[df["Status"] == "At Risk"]

    print("\n========== SUMMARY ==========")
    print(f"Average attendance: {average_attendance:.2f}%")
    print(f"Average marks: {average_marks:.2f}")
    print(f"At Risk students: {len(at_risk)}")

    if not at_risk.empty:
        print("At Risk names: " + ", ".join(at_risk["Name"].tolist()))
    else:
        print("At Risk names: None")

    # Chart 1: Bar chart of attendance percentage by student.
    plt.figure(figsize=(9, 5))
    plt.bar(df["Name"], df["Attendance_Percentage"])
    plt.axhline(
        y=ATTENDANCE_LIMIT,
        linestyle="--",
        label="75% attendance limit"
    )
    plt.title("Student Attendance Percentage")
    plt.xlabel("Student Name")
    plt.ylabel("Attendance (%)")
    plt.ylim(0, 105)
    plt.legend()
    plt.tight_layout()

    # Chart 2: Scatter chart of attendance versus marks.
    plt.figure(figsize=(9, 5))
    plt.scatter(
        df["Attendance_Percentage"],
        df["Marks"],
        s=80,
        label="Students"
    )
    for _, student in df.iterrows():
        plt.annotate(
            student["Name"],
            (student["Attendance_Percentage"], student["Marks"]),
            xytext=(5, 5),
            textcoords="offset points"
        )
    plt.axvline(
        x=ATTENDANCE_LIMIT,
        linestyle="--",
        label="75% attendance limit"
    )
    plt.axhline(
        y=MARKS_LIMIT,
        linestyle=":",
        label="40 marks limit"
    )
    plt.title("Attendance vs Marks")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Marks (out of 100)")
    plt.xlim(0, 105)
    plt.ylim(0, 105)
    plt.legend()
    plt.tight_layout()

    plt.show()


def main():
    print("==============================================")
    print(" STUDENT ATTENDANCE & PERFORMANCE TRACKER")
    print("==============================================")

    students = load_and_clean_data(CSV_FILE)

    if students.empty:
        print("\nNo valid data to analyse.")
        return

    while True:
        print("\nMENU")
        print("1. Student Report")
        print("2. Summary and Charts")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            display_report(students)
        elif choice == "2":
            display_summary_and_charts(students)
        elif choice == "3":
            print("Thank you for using the Student Tracker.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
