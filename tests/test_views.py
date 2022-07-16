from django.test import TestCase
from django.urls import reverse

from todo.models import Task


class AddNewTaskView(TestCase):

    def test_view_url_exists(self):
        resp = self.client.get('/add/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_accesible_by_name(self):
        resp = self.client.get(reverse('add-task'))
        self.assertEquals(resp.status_code, 200)

    def test_adding_task(self):
        resp = self.client.post('/add/', {
            "title": "test",
            "description": "smth",
            "accomplishmentDate": "2022-07-20"
        }, content_type="application/json")
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(resp.content, "Task created".encode())
        self.assertEquals(self.client.get(
            '/add/').content, "Wrong HTTP method".encode())


class CompleteTaskView(TestCase):

    @classmethod
    def setUpTestData(cls):
        Task.objects.create(
            title="Homework", description="I need to do my homework for tomorrow", accomplishmentDate='2019-08-02')

    def test_view_url_exists(self):
        resp = self.client.post('/complete/1/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_accesible_by_name(self):
        resp = self.client.post(
            reverse('complete-task', kwargs={'pk': Task.objects.first().id}))
        self.assertEquals(resp.status_code, 200)

    def test_task_accomplishment(self):
        default_accomplishment_value = Task.objects.first().completed
        self.assertEquals(default_accomplishment_value, False)
        id = Task.objects.first().id
        resp = self.client.post(f"/complete/{id}/")
        processed_task_accomplishment_value = Task.objects.first().completed
        self.assertEquals(processed_task_accomplishment_value, True)
        self.assertFalse(default_accomplishment_value,
                         processed_task_accomplishment_value)
        self.assertEquals(resp.content, 'Done'.encode())


class GetAllTasksView(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(3):
            Task.objects.create(
                title="Homework", description="I need to do my homework for tomorrow", accomplishmentDate='2019-08-02')

    def test_view_url_exists(self):
        resp = self.client.get('/all/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_accesible_by_name(self):
        resp = self.client.get(reverse('get-all-tasks',))
        self.assertEquals(resp.status_code, 200)

    def test_get_all_tasks(self):
        resp = self.client.get('/all/').json()
        for taskJson in resp:
            self.assertEquals(taskJson['fields']['title'], "Homework")
            self.assertEquals(taskJson['fields']['description'],
                              "I need to do my homework for tomorrow")
            self.assertEquals(taskJson['fields']
                              ['accomplishmentDate'], "2019-08-02")


class GetTaskView(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(
            title="Homework", description="I need to do my homework for tomorrow", accomplishmentDate='2019-08-02')

    def test_view_url_exists(self):
        id = Task.objects.first().id
        resp = self.client.get(f"/get/{id}/")
        self.assertEquals(resp.status_code, 200)

    def test_view_url_accesible_by_name(self):
        resp = self.client.get(
            reverse('get-task', kwargs={'pk': Task.objects.first().id}))
        self.assertEquals(resp.status_code, 200)

    def test_get_task(self):
        id = Task.objects.first().id
        resp = self.client.get(f"/get/{id}/").json()
        self.assertEquals(resp[0]['fields']['title'], "Homework")
        self.assertEquals(resp[0]['fields']['description'],
                          "I need to do my homework for tomorrow")
        self.assertEquals(resp[0]
                          ['fields']['accomplishmentDate'], "2019-08-02")


class DeleteTaskView(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(
            title="Homework", description="I need to do my homework for tomorrow", accomplishmentDate='2019-08-02')

    def test_view_url_exists(self):
        id = Task.objects.first().id
        resp = self.client.delete(f"/delete/{id}/")
        self.assertEquals(resp.status_code, 200)

    def test_view_url_accesible_by_name(self):
        resp = self.client.delete(
            reverse('delete-task', kwargs={'pk': Task.objects.first().id}))
        self.assertEquals(resp.status_code, 200)

    def test_delete_task(self):
        self.assertEquals(Task.objects.exists(), True)

        id = Task.objects.first().id
        self.assertNotEquals(Task.objects.filter(id=id), None)

        resp = self.client.delete(f"/delete/{id}/")
        self.assertEquals(resp.content, "Task Deleted".encode())
        self.assertEquals(Task.objects.exists(), False)
