from new_student import Student

def test_student_creation():
    """
    Test the creation of Student objects.
    """
    # Test creating a student without providing an ID
    student1 = Student(name="Edward", surname="Agle")
    print(student1)

    # Test attempting to create a student with an ID (should raise TypeError)
    try:
        student2 = Student(name="Edward", surname="Agle", id="toto")
        print(student2)
    except TypeError as e:
        print(f"Error: {e}")

def main():
    """
    Main function to run tests.
    """
    test_student_creation()

if __name__ == "__main__":
    main()
