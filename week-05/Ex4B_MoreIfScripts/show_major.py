''' Lab 5 '''

student_name = input("Enter your name: ")
student_major = input(f"Hello {student_name}!, please enter your major code: ").upper()

major_name = ""
dep_office_location = ""

match student_major:
    case "BIOL":
        major_name = "Biology"
        dep_office_location = "Science Bldg, Room 310"

    case "CSCI":
        major_name = "Computer Science"
        dep_office_location = "Sheppard Hall, Room 314"

    case "ENG":
        major_name = "English"
        dep_office_location = "Kerr Hall, Room 201"

    case "HIST":
        major_name = "History"
        dep_office_location = "Kerr Hall, Room 114"

    case "MKT":
        major_name = "Marketing"
        dep_office_location = "Westly Hall, Room 310"

    case _:
        major_name = "<unknown>"


print(
    f"\nThe name of the major: {major_name}\n"
    f"Department's office location: {dep_office_location}"
)