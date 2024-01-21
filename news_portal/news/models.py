from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

article = 'AR'
news = 'NE'
post_type = [(article, 'статья'),
             (news, 'новость')]


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        rating_posts = sum(post.rating * 3 for post in Post.objects.filter(author=self))
        rating_authors_comments = sum(comment.rating for comment in Comment.objects.filter(post__author=self))
        rating_users_comments = sum(comment.rating for post in Post.objects.filter(author=self) for comment in
                                    Comment.objects.filter(post=post))

        self.rating = rating_posts + rating_users_comments + rating_authors_comments
        self.save()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    objects = None
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=post_type)
    timedate = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        preview_length = 124
        if len(self.text) > preview_length:
            return f"{self.text[:preview_length]}..."
        else:
            return self.text

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.pk)])

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    timedate = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

