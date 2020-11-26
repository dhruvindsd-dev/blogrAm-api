from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profile images',
                            height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.user


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    content = models.TextField()
    img = models.ImageField(upload_to='blogImages',
                            null=True, default=None, blank=True)

    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, default=None)
    tags = models.ManyToManyField(Tag)

# def __str__(self):
#     return f"{self.title} : [{self.user}]"

# def save(self, *args, **kwargs):
#     if not self.id:
#         self.img = self.compressImage(self.img)
#     super(Blog, self).save(*args, **kwargs)

# def compressImage(self, uploadedImage):
#     imageTemproary = Image.open(uploadedImage)
#     outputIoStream = BytesIO()
#     imageTemproaryResized = imageTemproary.resize((1020, 573))
#     imageTemproary.save(outputIoStream, format='JPEG', quality=65)
#     outputIoStream.seek(0)
#     uploadedImage = InMemoryUploadedFile(outputIoStream, 'ImageField', "%s.jpg" % uploadedImage.name.split('.')[
#                                          0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
#     return uploadedImage
