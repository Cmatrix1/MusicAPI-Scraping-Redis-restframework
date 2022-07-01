from django.db import models

class Searches(models.Model):
    query = models.CharField(max_length=150)
    time = models.DateTimeField(auto_now_add=True)
    # user = models.GenericIPAddressField(_(""), protocol="both", unpack_ipv4=False)

    def __str__(self):
        return self.name

