attendance = float(input("Enter attendance percentage: "))
marks = int(input("Enter internal marks: "))
lab = input("Labs completed? (yes/no): ").lower()
fees = input("Fees cleared? (yes/no): ").lower()

if (attendance >= 75 and marks >= 40
        and lab == "yes" and fees == "yes"):
    print("Eligible for Examination")
else:
    print("Not Eligible")

    if attendance < 75:
        print("Attendance is insufficient")
    if marks < 40:
        print("Internal marks are insufficient")
    if lab != "yes":
        print("Laboratory work incomplete")
    if fees != "yes":
        print("Fees not cleared")