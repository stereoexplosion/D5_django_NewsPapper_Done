from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        posts = Post.objects.filter(author=self.id)  # все посты автора
        post_rating = sum([r.post_rating * 3 for r in posts])  # рейтинг каждого поста автора умножен на 3
        comment_rating = sum([r.comment_rating for r in
                               Comment.objects.filter(author_id=self.id)])  # сумма лайков/дислайков к комментам автора
        all_to_post_comment_rating = sum([r.comment_rating for r in Comment.objects.filter(
            post__in=posts)])  # сумма лайков/дислайков всех комментов к постам автора
        self.author_rating == post_rating + comment_rating + all_to_post_comment_rating

    def __str__(self):
        return self.author.username

class Category(models.Model):
    news_category = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.news_category

class Post(models.Model):
    article = 'Article'
    news = 'News'
    POSITIONS = [
        (article, 'Статья'),
        (news, 'Новость')]

    author_post = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_category = models.ManyToManyField(Category)
    post_type_select = models.CharField(max_length=32, choices=POSITIONS, default=news)
    post_heading = models.CharField(max_length=64)
    post_text = models.TextField()
    post_create_date = models.DateTimeField(auto_now_add=True)
    post_rating = models.IntegerField(default=0)

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        preview_length = 124
        if len(self.post_text) > preview_length:
            preview_string = self.post_text[:preview_length] + '...'
        else:
            preview_string = self.post_text
        return preview_string

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    comment_text = models.CharField(max_length=256)
    comment_create_date = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()


