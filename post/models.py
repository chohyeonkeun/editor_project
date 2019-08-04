from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
from django.contrib.auth import get_user_model

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')

    '''    
    related_name은 내가 참조하고 있는 모델에 attribute 속성값이 생기게 됨 (ex. user.posts)
    '''

    title = models.CharField(max_length=100)
    text = RichTextUploadingField()  # 글 작성 편리하게 해주는 에디터 사용 위해 RichTextField 사용
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)