from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)

    img_src = models.URLField(null=True, blank=True)

    philanthropy_req = models.IntegerField(default='0')
    professional_req = models.IntegerField(default='0')
    tech_req = models.IntegerField(default='0')
    financial_req = models.BooleanField(default=False)

    pledge_class = models.TextField(max_length=5, blank=False)

    FRESHMAN = 0
    SOPHOMORE = 1
    JUNIOR = 2
    SENIOR = 3
    COLLEGE_YEAR = ((FRESHMAN, "Freshman"), (SOPHOMORE, "Sophomore"), (JUNIOR, "Junior"), (SENIOR, "Senior"))
    college_year_selection = models.PositiveSmallIntegerField(choices=COLLEGE_YEAR, null=False, blank=False, default=0)

    def get_college_year(self):
        try:
            return self.COLLEGE_YEAR[self.college_year_selection][1]
        except Exception:
            return "N/A"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()