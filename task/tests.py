from django.test import TestCase
from models import Task

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