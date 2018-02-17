from django.db import models

class Author(models.Model):
  '''
  Author model.
  '''

  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  birth_date = models.DateField(null=True, blank=True)
  nationality = models.CharField(max_length=100)

  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)

  def __str__(self):
    return "%s %s" % (self.first_name, self.last_name)

class Book(models.Model):
  """
  Book model.
  """


  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  title = models.CharField(max_length=255, )
  sinopsis = models.TextField(null=True, blank=True)
  publication_date = models.DateField(null=True, blank=True)

  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title