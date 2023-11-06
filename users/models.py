
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_save

class CustomUser(AbstractUser, PermissionsMixin):
    user_type_data=(('Admin', 'Admin'), ('Secretary', 'Secretary'), ('Instructor', 'Instructor'), ('Student', 'Student'))

    user_type=models.CharField(default='Admin',choices=user_type_data,max_length=30)
    

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    
class Secretary(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    
class RDV(models.Model):
    id = models.AutoField(primary_key=True)
    rdv_name = models.CharField(max_length=30)
    duration = models.TimeField()
    start_at = models.DateTimeField(auto_now=True)
    secretary_id = models.ForeignKey(Secretary, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
class Instructor(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)        
    rdv_id = models.ForeignKey(RDV, on_delete=models.DO_NOTHING)
    objects=models.Manager()

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    forfait = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    rdv_id = models.ForeignKey(RDV, on_delete=models.DO_NOTHING)
    objects=models.Manager()

class Forfait(models.Model):
    id = models.AutoField(primary_key=True)
    forfait_hours = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class StudentMessage():
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

class SecretaryMessage():
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Secretary, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'Admin':
            Admin.objects.create(admin=instance)
        if instance.user_type == 'Secretary':
            Secretary.objects.create(admin=instance,address='')
        if instance.user_type == 'Instructor':
            Instructor.objects.create(admin=instance,rdv_id=RDV.objects.get(id=1),address='')
        if instance.user_type == 'Student':
            Student.objects.create(admin=instance,rdv_id=RDV.objects.get(id=1),address='')

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 'Admin':
        instance.admin.save()
    if instance.user_type == 'Secretary':
        instance.secretary.save()
    if instance.user_type == 'Instructor':
        instance.instructor.save()
    if instance.user_type == 'Student':
        instance.student.save()