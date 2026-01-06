import csv

with open("Data.csv", "r") as file:
    reader = csv.DictReader(file)

    with open("result.txt", "w") as result_file:
        for row in reader:
            name = row["name"]

            marks = [
                int(row["mark1"]),
                int(row["mark2"]),
                int(row["mark3"]),
                int(row["mark4"]),
                int(row["mark5"])
            ]

            total = sum(marks)
            average = total / len(marks)

            if average >= 35:
                result = "Pass"
            else:
                result = "Fail"

            result_file.write(
                f"Name: {name}, Total: {total}, Average: {average}, Result: {result}\n"
            )
