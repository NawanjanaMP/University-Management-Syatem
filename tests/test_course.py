# tests/test_course.py

import pytest
from models.course import Course
from models.student import SecureStudentRecord

def test_course_enrollment_limit():
    course = Course("T101", "Test Course", 3, 1)
    student1 = SecureStudentRecord("Student One", 1, "s1@uni.edu", "Major")
    student2 = SecureStudentRecord("Student Two", 2, "s2@uni.edu", "Major")

    assert not course.is_full()
    course.add_student(student1)
    assert course.is_full()
    
    with pytest.raises(OverflowError):
        course.add_student(student2)