from django.db import models

class Blog(models.Model):

    title=models.CharField(max_length=200)
    put_date=models.DateTimeField()
    body=models.TextField()
    image = models.ImageField(upload_to='imagesBlog/')
    def summary(self):
        return self.body[:100]
    def put_date_pretty(self):
        return self.put_date.strftime('%b %e %y')
    def __str__(self):
        return self.title
