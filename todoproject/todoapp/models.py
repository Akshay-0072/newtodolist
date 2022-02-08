from django.db import models

class TodoListItem(models.Model):
    taskTitle = models.CharField(max_length=20,default='')
    taskDesc = models.CharField(max_length=60,default='')
    time = models.DateTimeField(auto_now_add=True)