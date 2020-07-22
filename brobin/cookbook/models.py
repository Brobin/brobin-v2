from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Recipe(models.Model):
    title = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default='', blank=True, max_length=128)
    notes = models.TextField()
    prep_time = models.IntegerField(blank=True, null=True)
    cook_time = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def total_time(self):
        return self.prep_time + self.cook_time
    
    @property
    def url(self):
        return self.get_absolute_url()


class Ingredient(models.Model):
    name = models.CharField(max_length=128, unique=True)
    recipe = models.ManyToManyField(Recipe, through='IngredientAmount')

    def __str__(self):
        return self.name


class IngredientAmount(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="ingredients", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.CharField(max_length=32)
    order = models.IntegerField(default=5)

    def __str__(self):
        return '{0} {1}'.format(self.amount, self.ingredient)

    class Meta:
        ordering = ['order']


class Step(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="steps", on_delete=models.CASCADE)
    text = models.TextField()
    order = models.IntegerField(default=5)

    class Meta:
        ordering = ['order']

