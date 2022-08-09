from django.db import models
from django.contrib.auth.models import User

class profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length = 20, verbose_name = 'Phone Number')
    
    M = 1
    F = 2
    P = 3
    N = 4
    GENDER_CHOICE = [
        (M, 'Male'), 
        (F, 'Female'),
        (P, 'Prefer not to say'),
        (N, 'Non-Binary')
    ]
    gender = models.IntegerField('Gender', choices=GENDER_CHOICE)
    birth_date = models.DateField('Birth date', blank=True, null=True)
    address = models.TextField('Address', blank=True, null=True)
    Image = models.ImageField('Profile Photo', upload_to = 'user/profile_Images')
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.user.get_full_name()
    def get_balance_display(self):
        return f'{self.balance} $'
    def deposit(self, amount):
        self.balance += amount
        self.save()
    def spend(self, amount):
        if self.balance < amount:
            return False
        else:
            self.balance -= amount
            self.save()
        
