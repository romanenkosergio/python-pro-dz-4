from faker import Faker
from .models import Student

fake = Faker()


def generate_student_service(count=1):
    """Generate user(s) based on the count parameter."""

    try:
        count = int(count)
        # Check if count is less than 100 and greater than 0
        if count > 100 or count < 1:
            return ValueError('Count must be less than 100 and greater than 0')

        students = []
        # Create a list of students
        for _ in range(count):
            students.append(
                Student(
                    first_name=fake.first_name(), last_name=fake.last_name(), age=fake.random_int(min=18, max=99)
                )
            )

        # Create student or students
        Student.objects.bulk_create(
            students
        )
        # Get the last :count students
        students = Student.objects.all().order_by('-id')[:count].values()

        return students

    except ValueError:
        return ValueError('Count must be an integer')

