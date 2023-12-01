from django.test import TestCase
from datetime import datetime


from app.models.headings import Heading


def create_a_heading_object(heading: str, created: datetime, updated: datetime, /) -> Heading:
    return Heading.objects.create(
        heading=heading,
        created=created,
        updated=updated
    )

class HeadingSingleObjectTestCase(TestCase):
    
    def test_heading_count_1(self):
        """
        Total test are zero
        """
        headings = Heading.objects.all()
        self.assertEqual(len(headings), 0)

    
    def create_a_test_object(self) -> None:
        # Create a heading object
        heading = "Time 1"
        heading_object = create_a_heading_object(
            heading,
            datetime.now().isoformat(),
            datetime.now().isoformat()
        )
        return heading_object

    def test_create_a_object(self):
        heading_object = self.create_a_test_object()
        self.assertEqual(
            heading_object.heading, "Time 1"
        )

    def test_heading_count_2(self):
        heading_object = self.create_a_test_object()
        
        self.assertEqual(len(Heading.objects.all()), 1)