from django.db import models
from PIL import Image
from django.utils.encoding import force_text, python_2_unicode_compatible
import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images/', filename)


# Create your models here.
@python_2_unicode_compatible
class Bigs(models.Model):
	user = models.ForeignKey('auth.User')
	topic = models.CharField(u'事件',max_length=160)
	year = models.CharField(u'年代',max_length=50)
	date = models.CharField(u'时间',max_length=50)
	era = models.CharField(u'朝代',max_length=80)
	place = models.CharField(u'地点',max_length=80)
	roles = models.CharField(u'人物',max_length=254)
	content = models.TextField(u'详情')
	refs = models.ForeignKey('Refs')
	memo = models.TextField(u'备注')
	comments = models.TextField(u'点评')
	image = models.ImageField(u'事件图片',upload_to=get_file_path)
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
	status = models.SmallIntegerField(default=1)

	def __str__(self):
		return self.topic


@python_2_unicode_compatible
class Refs(models.Model):
    name = models.CharField(u'名称',max_length=100)
    author = models.CharField(u'作者',max_length=100)
    publisher = models.CharField(u'出版社',max_length=100)
    pubtime = models.DateTimeField(u'出版时间')
    intro = models.TextField(u'简介')
    cover = models.ImageField(u'封面',upload_to=get_file_path)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.name
