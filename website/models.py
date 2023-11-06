from django.db import models


class Services(models.Model):
    s_name = models.CharField(max_length=100)
    s_description = models.CharField(max_length=250)
    s_price = models.IntegerField()
    objects = models.Manager()

    class Meta:
        db_table = 'services_offered'


class Room(models.Model):
    a1 = models.CharField(max_length=100)
    a2 = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # objects = models.Manager()


class User(models.Model):
    # null is for DB & blank is for HTML
    u_id = models.CharField(max_length=20, blank=False, null=False)
    u_name = models.CharField(max_length=100, blank=False, null=False)
    u_email = models.EmailField(blank=False, null=False)
    u_contact = models.CharField(max_length=15, null=False)
    # objects = models.Manager()

    class Meta:
        db_table = "user"
