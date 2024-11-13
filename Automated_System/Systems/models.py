from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, null=True, blank=True)


class Service(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.TextField()
    service_price = models.DecimalField(max_digits=10, decimal_places=2)
    service_duration = models.DurationField(help_text='Duration of the service in minutes.')
    service_image = models.ImageField(upload_to='service_images/', blank=True)
    service_category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.service_name
    

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    appointment_status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Scheduled')
    appointment_created = models.DateTimeField(auto_now_add=True)
    appointment_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + ' - ' + self.service.service_name + ' - ' + str(self.appointment_date) + ' - ' + str(self.appointment_time)
    

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_message = models.TextField()
    notification_created = models.DateTimeField(auto_now_add=True)
    notification_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + ' - ' + self.notification_message[:20]
    

class Register(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    register_date = models.DateField(auto_now_add=True)
    register_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' - ' + str(self.register_date) + ' - ' + str(self.register_time)
    
class Login(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_date = models.DateField(auto_now_add=True)
    login_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' - ' + str(self.login_date) + ' - ' + str(self.login_time)

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    feedback_rating = models.SmallIntegerField()
    feedback_date = models.DateField(auto_now_add=True)
    feedback_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' - ' + str(self.feedback_date) + ' - ' + str(self.feedback_time)



    