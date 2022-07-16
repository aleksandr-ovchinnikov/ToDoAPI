from django.test import TestCase
from todo.models import Task


class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(
            title="Homework", description="I need to do my homework for tomorrow", accomplishmentDate='2019-08-02')

    def test_title_label(self):
        task = Task.objects.get(id=1)
        title_lable = task._meta.get_field('title').verbose_name
        self.assertEquals(title_lable, 'title')

    def test_title_max_length(self):
        task = Task.objects.get(id=1)
        max_lenght = task._meta.get_field('title').max_length
        self.assertEquals(max_lenght, 100)

    def test_description_label(self):
        task = Task.objects.get(id=1)
        description_lable = task._meta.get_field('description').verbose_name
        self.assertEquals(description_lable, 'description')

    def test_descrtiption_max_length(self):
        task = Task.objects.get(id=1)
        max_lenght = task._meta.get_field('description').max_length
        self.assertEquals(max_lenght, 500)

    def test_accomplishment_date_label(self):
        task = Task.objects.get(id=1)
        accomplishment_date_lable = task._meta.get_field(
            'accomplishmentDate').verbose_name
        self.assertEquals(accomplishment_date_lable, 'accomplishmentDate')

    def test_completed_label(self):
        task = Task.objects.get(id=1)
        completed_lable = task._meta.get_field('completed').verbose_name
        self.assertEquals(completed_lable, 'completed')

    def test_default_completed_value(self):
        task = Task.objects.get(id=1)
        default_value = task.completed
        self.assertEquals(default_value, False)

    def test_object_name_is_title(self):
        task = Task.objects.get(id=1)
        expected_object_name = task.title
        self.assertEquals(expected_object_name, str(task))
