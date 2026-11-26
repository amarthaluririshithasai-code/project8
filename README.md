# Project 8 – Examination Eligibility System

## Description
The Examination Eligibility System is a Python-based program designed to determine whether a student is eligible to attend the final examination. It checks the student's attendance percentage, internal marks, laboratory completion, and fee payment status.

The program evaluates all eligibility requirements and displays whether the student is eligible or not eligible for the final examination.

## Objectives
- To calculate the student's attendance percentage.
- To check the minimum attendance requirement.
- To verify internal examination marks.
- To check laboratory completion status.
- To verify fee payment status.
- To determine the student's final examination eligibility.

## Concepts Used
- Variables and data types
- Arithmetic operators
- Conditional statements (`if`, `elif`, `else`)
- Logical operators (`and`)
- User input and output
- Input validation

## Eligibility Criteria

| Requirement | Minimum Condition |
|---|---|
| Attendance | 75% or above |
| Internal Marks | 40 or above |
| Laboratory Completion | Completed |
| Fee Payment | Paid |

*Note: These are the sample eligibility assumptions used in this program.*

## Sample Output 1 – Eligible Student

```text
Enter student name: Ravi
Enter total classes: 100
Enter attended classes: 85
Enter internal marks: 45
Are all labs completed? yes
Are fees paid? yes

----- EXAMINATION ELIGIBILITY RESULT -----

Student Name: Ravi
Attendance Percentage: 85.00%
Internal Marks: 45
Laboratory Status: Completed
Fee Status: Paid

Result: ELIGIBLE FOR FINAL EXAMINATION
```

## Sample Output 2 – Not Eligible Student

```text
Enter student name: Ravi
Enter total classes: 100
Enter attended classes: 60
Enter internal marks: 45
Are all labs completed? yes
Are fees paid? yes

----- EXAMINATION ELIGIBILITY RESULT -----

Student Name: Ravi
Attendance Percentage: 60.00%
Internal Marks: 45
Laboratory Status: Completed
Fee Status: Paid

Result: NOT ELIGIBLE FOR FINAL EXAMINATION
Reason: Attendance requirement not satisfied.
```

## How to Run
1. Download or clone this repository.
2. Open the project folder in Visual Studio Code.
3. Open the Python file `Case_39_Exam_Eligibility.py`.
4. Run the program using Python.
5. Enter the student's details when prompted.
6. View the final examination eligibility result.

## Output Screenshots
The output screenshots demonstrate the eligibility checking process.

- `Examination-Eligibility-Output-1.png`
- `Examination-Eligibility-Output-2.png`

## Conclusion
The Examination Eligibility System successfully determines whether a student is eligible to attend the final examination by checking attendance, internal marks, laboratory completion, and fee payment status.

This project demonstrates the practical use of variables, arithmetic operators, conditional statements, logical operators, and input validation in Python programming.
