MAX_STUDENTS = 100
PASSING_GRADE = 75
subjects = ["Math", "Science", "English", "MAPEH", "Filipino"]


def input_scores(num_students):
    if num_students > MAX_STUDENTS:
        print(f"Error: Maximum number of students is {MAX_STUDENTS}")
        return None

    students_scores = []
    for i in range(num_students):
        print(f"\nEnter scores for student {i + 1}:")
        scores = {}
        for subject in subjects:
            while True:
                try:
                    score = float(input(f"  {subject}: "))
                    if 0 <= score <= 100:
                        scores[subject] = score
                        break
                    else:
                        print("Score must be between 0 and 100")
                except ValueError:
                    print("Please enter a valid number")
        students_scores.append(scores)
    return students_scores


def calculate_averages(students_scores):
    for student in students_scores:
        total = sum(student[subject] for subject in subjects)
        student["Average"] = total / len(subjects)


def count_pass_fail(students_scores):
    passed = sum(
        1 for student in students_scores if student["Average"] >= PASSING_GRADE)
    failed = len(students_scores) - passed
    return passed, failed


def find_highest_average(students_scores):
    highest_avg = -1
    highest_idx = -1

    for idx, student in enumerate(students_scores, start=1):
        if student["Average"] > highest_avg:
            highest_avg = student["Average"]
            highest_idx = idx

    return highest_avg, highest_idx


def print_header():
    header = ["Student No."]
    header.extend(subjects)
    header.extend(["Average", "Status"])

    width = len(header) * 12 + 2

    print("\nResults:")
    print("=" * width)
    print("".join(f"{col:<12}" for col in header))
    print("-" * width)


def main():
    # Input number of students
    while True:
        try:
            num_students = int(
                input("Enter the number of students (max 100): "))
            if 0 < num_students <= MAX_STUDENTS:
                break
            print(f"Please enter a number between 1 and {MAX_STUDENTS}")
        except ValueError:
            print("Please enter a valid number")

    # Get scores
    students_scores = input_scores(num_students)
    if students_scores is None:
        return

    calculate_averages(students_scores)

    passed, failed = count_pass_fail(students_scores)

    highest_avg, highest_idx = find_highest_average(students_scores)

    print_header()

    # Display individual scores in table rows
    for idx, scores in enumerate(students_scores, start=1):
        row = [f"{idx:02d}"]
        for subject in subjects:
            row.append(f"{scores[subject]:.2f}")
        row.append(f"{scores['Average']:.2f}")
        status = "Pass" if scores['Average'] >= PASSING_GRADE else "Fail"
        row.append(status)
        print("".join(f"{col:<12}" for col in row))

    width = len(subjects) * 12 + 38

    print("=" * width)
    print("\nSummary:")
    print("=" * width)
    print(f"Number of students who passed: {passed}")
    print(f"Number of students who failed: {failed}")
    print(f"Highest average: {highest_avg:.2f} (Student {highest_idx})")
    print("=" * width)


if __name__ == "__main__":
    main()
