from django.db import models


class ImageDetection(models.Model):

    uploaded_image = models.ImageField(upload_to='uploads/')

    output_image = models.ImageField(upload_to='outputs/', blank=True, null=True)

    

    def __str__(self):

        return f"Image Detection {self.id}"

