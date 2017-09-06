from django.test import TestCase
from models import Task
from django.test.client import Client
from django.urls import reverse

class TaskTest(TestCase):
    def test_add_task(self):
        """
        
        """
        # given
        init_len = len(Task.objects.all())

        # when
        task = Task.objects.create(description="Afeitar al gato")

        # then
        self.assertEqual(init_len + 1, len(Task.objects.all()))
        self.assertTrue(Task.objects.filter(description="Afeitar al gato").exists())

    def test_delete_task(self):
        # given
        task = Task.objects.create(description="hola mundo")
        task_len = len(Task.objects.all())

        # when
        Task.objects.get(description="hola mundo").delete()

        # then
        self.assertEqual(task_len - 1, len(Task.objects.all()))
        self.assertFalse(Task.objects.filter(description="hola mundo").exists())
        
    def test_edit_task(self):
        # given
        task = Task.objects.create(description="Afeitar al gato")
        
        #when
        t = Task.objects.get(description="Afeitar al gato")
        t.description="Afeitar al perro"
        t.save()
        
        # then
        self.assertTrue(Task.objects.filter(description="Afeitar al perro").exists())
class TaskViewsTest(TestCase):
    
    def setUp(self):
        self.description = "Afeitar al perro"
        self.task = Task.objects.create(description=self.description)
        
    
    def test_delete(self):
        # given 
        # a client
        client = Client()
        
        # when
        # the client makes a post request with a task id
        client.post(path=reverse("delete_task"), data={"id":self.task.id})
        
        # then
        # the task is deleted
        self.assertFalse(Task.objects.filter(description=self.description).exists())
        
    def test_delete_unexisting_task(self):
        # given
        # a client
        client = Client()
        init_len = Task.objects.all().count()
        
        # when
        # the client makes a post request with a task id that doesnt exist
        client.post(path=reverse("delete_task"), data={"id":"this is not an id"})
        
        # then
        # there is no changes
        self.assertEqual(init_len, Task.objects.all().count())