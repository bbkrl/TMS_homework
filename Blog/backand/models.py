from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=50, null=False, blank=False, unique=True)

    def __str__(self):
        return f'{self.title}'


class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.username}'


class Author(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author')
    activity = models.CharField(max_length=50, null=False, blank=False)
    company = models.CharField(max_length=50, null=False, blank=False)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.user_id}'


class Reader(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    # user_id = models.IntegerField(unique=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='reader')

    def __str__(self):
        return f'{self.user_id}'


class Post(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    create_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    update_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateField(auto_now=True)
    title = models.CharField(max_length=120, null=False, blank=False)
    text = models.TextField(blank=False)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.title} created at: {self.create_at} update at: {self.update_at}'


class Comment(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    update_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateField(auto_now=True)
    text = models.TextField(blank=False)

    def __str__(self):
        return f'user:{self.user_id} post:{self.post_id} {self.create_at}'


class Subscription(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    subscriber_user_id = models.ForeignKey(Reader, on_delete=models.CASCADE)
    subscription_user_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return f'{self.subscriber_user_id} подписан на {self.subscription_user_id}'

#  TODO реализовать лайки
