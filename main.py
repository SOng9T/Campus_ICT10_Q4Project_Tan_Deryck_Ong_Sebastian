# main.py - External Python module for Attendance Tracker

def count_present(students_list):
    """Return the number of students marked as Present"""
    count = 0
    for student in students_list:
        if student["status"] == "Present":
            count = count + 1
    return count

def count_absent(students_list):
    """Return the number of students marked as Absent"""
    total = len(students_list)
    present = count_present(students_list)
    return total - present

def get_attendance_percentage(students_list):
    """Return attendance percentage"""
    if len(students_list) == 0:
        return 0
    present = count_present(students_list)
    return (present / len(students_list)) * 100