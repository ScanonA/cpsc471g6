# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ad(models.Model):
    link = models.ForeignKey('Post', models.DO_NOTHING, db_column='Link', primary_key=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=140, blank=True, null=True)  # Field name made lowercase.
    num_views = models.IntegerField(db_column='Num_views', blank=True, null=True)  # Field name made lowercase.
    num_clicks = models.IntegerField(db_column='Num_clicks', blank=True, null=True)  # Field name made lowercase.
    email_address = models.ForeignKey('LoggedIn', models.DO_NOTHING, db_column='Email_address')  # Field name made lowercase.
    name = models.ForeignKey('User', models.DO_NOTHING, db_column='Name')  # Field name made lowercase.
    id = models.ForeignKey('User', models.DO_NOTHING, db_column='ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad'


class Admin(models.Model):
    email_address = models.ForeignKey('LoggedIn', models.DO_NOTHING, db_column='Email_address', primary_key=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=128)  # Field name made lowercase.
    name = models.ForeignKey('User', models.DO_NOTHING, db_column='Name')  # Field name made lowercase.
    id = models.ForeignKey('User', models.DO_NOTHING, db_column='ID')  # Field name made lowercase.
    ip_address = models.CharField(db_column='IP_Address', max_length=45)  # Field name made lowercase.
    employee_id = models.IntegerField(db_column='Employee_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'
        unique_together = (('name', 'id', 'employee_id'),)


class Advertiser(models.Model):
    email_address = models.ForeignKey('LoggedIn', models.DO_NOTHING, db_column='Email_address', primary_key=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=128)  # Field name made lowercase.
    name = models.ForeignKey('User', models.DO_NOTHING, db_column='Name')  # Field name made lowercase.
    id = models.ForeignKey('User', models.DO_NOTHING, db_column='ID')  # Field name made lowercase.
    ip_address = models.CharField(db_column='IP_Address', max_length=45)  # Field name made lowercase.
    company_name = models.CharField(db_column='Company_name', max_length=48)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'advertiser'
        unique_together = (('name', 'id', 'company_name'),)


class Comment(models.Model):
    ctext = models.CharField(db_column='CText', max_length=140, blank=True, null=True)  # Field name made lowercase.
    name = models.ForeignKey('User', models.DO_NOTHING, db_column='Name')  # Field name made lowercase.
    id = models.ForeignKey('User', models.DO_NOTHING, db_column='ID')  # Field name made lowercase.
    link = models.ForeignKey('Post', models.DO_NOTHING, db_column='Link', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comment'
        unique_together = (('name', 'id'),)


class Contains(models.Model):
    name = models.ForeignKey('Thread', models.DO_NOTHING, db_column='Name')  # Field name made lowercase.
    link = models.ForeignKey('Post', models.DO_NOTHING, db_column='Link')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contains'
        unique_together = (('name', 'link'),)


class Follow(models.Model):
    email_address1 = models.ForeignKey('LoggedIn', models.DO_NOTHING, db_column='Email_address1')  # Field name made lowercase.
    email_address2 = models.ForeignKey('LoggedIn', models.DO_NOTHING, db_column='Email_address2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'follow'
        unique_together = (('email_address1', 'email_address2'),)


class LoggedIn(models.Model):
    email_address = models.CharField(db_column='Email_address', primary_key=True, max_length=255)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=128)  # Field name made lowercase.
    name = models.ForeignKey('User', models.DO_NOTHING, db_column='Name')  # Field name made lowercase.
    id = models.ForeignKey('User', models.DO_NOTHING, db_column='ID')  # Field name made lowercase.
    ip_address = models.CharField(db_column='IP_Address', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logged_in'
        unique_together = (('name', 'id'),)


class Moderates(models.Model):
    name = models.ForeignKey('Thread', models.DO_NOTHING, db_column='Name')  # Field name made lowercase.
    email_address = models.ForeignKey(LoggedIn, models.DO_NOTHING, db_column='Email_address')  # Field name made lowercase.
    email_address2 = models.ForeignKey(LoggedIn, models.DO_NOTHING, db_column='Email_address2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'moderates'
        unique_together = (('name', 'email_address', 'email_address2'),)


class Picture(models.Model):
    link = models.ForeignKey('Post', models.DO_NOTHING, db_column='Link', primary_key=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=140, blank=True, null=True)  # Field name made lowercase.
    resolution = models.CharField(db_column='Resolution', max_length=16)  # Field name made lowercase.
    name = models.ForeignKey('User', models.DO_NOTHING, db_column='Name')  # Field name made lowercase.
    id = models.ForeignKey('User', models.DO_NOTHING, db_column='ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'picture'


class Post(models.Model):
    link = models.CharField(db_column='Link', primary_key=True, max_length=255)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=140, blank=True, null=True)  # Field name made lowercase.
    email_address = models.ForeignKey(LoggedIn, models.DO_NOTHING, db_column='Email_address', blank=True, null=True)  # Field name made lowercase.

    @models.permalink
    def get_absolute_url(self):
        return ('blog_post_detail', (),
            {
                'slug': self.slug,
            })
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.caption)
            super(Post, self).save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'post'
        ordering = ['email_address']
        def __unicode__(self):
            return self.caption


class Report(models.Model):
    link = models.ForeignKey(Post, models.DO_NOTHING, db_column='Link')  # Field name made lowercase.
    name = models.ForeignKey('User', models.DO_NOTHING, db_column='Name')  # Field name made lowercase.
    id = models.ForeignKey('User', models.DO_NOTHING, db_column='ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'report'
        unique_together = (('link', 'name', 'id'),)


class Repost(models.Model):
    link = models.ForeignKey(Post, models.DO_NOTHING, db_column='Link')  # Field name made lowercase.
    name = models.ForeignKey('User', models.DO_NOTHING, db_column='Name')  # Field name made lowercase.
    id = models.ForeignKey('User', models.DO_NOTHING, db_column='ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'repost'
        unique_together = (('link', 'name', 'id'),)


class SubscribesTo(models.Model):
    name = models.ForeignKey('Thread', models.DO_NOTHING, db_column='Name')  # Field name made lowercase.
    email_address = models.ForeignKey(LoggedIn, models.DO_NOTHING, db_column='Email_address')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subscribes_to'
        unique_together = (('name', 'email_address'),)


class Tag(models.Model):
    link = models.ForeignKey(Post, models.DO_NOTHING, db_column='Link')  # Field name made lowercase.
    tagtext = models.CharField(db_column='Tagtext', max_length=24)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tag'
        unique_together = (('link', 'tagtext'),)


class Thread(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=16)  # Field name made lowercase.
    email_address = models.ForeignKey(LoggedIn, models.DO_NOTHING, db_column='Email_address')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'thread'


class User(models.Model):
    name = models.CharField(db_column='Name', max_length=16)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    ip_address = models.CharField(db_column='IP_Address', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
        unique_together = (('name', 'id'),)


class Video(models.Model):
    link = models.ForeignKey(Post, models.DO_NOTHING, db_column='Link', primary_key=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=140, blank=True, null=True)  # Field name made lowercase.
    resolution = models.CharField(db_column='Resolution', max_length=16)  # Field name made lowercase.
    length = models.IntegerField(db_column='Length')  # Field name made lowercase.
    name = models.ForeignKey(User, models.DO_NOTHING, db_column='Name')  # Field name made lowercase.
    id = models.ForeignKey(User, models.DO_NOTHING, db_column='ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'video'


class Vote(models.Model):
    link = models.ForeignKey(Post, models.DO_NOTHING, db_column='Link')  # Field name made lowercase.
    name = models.ForeignKey(User, models.DO_NOTHING, db_column='Name')  # Field name made lowercase.
    id = models.ForeignKey(User, models.DO_NOTHING, db_column='ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vote'
        unique_together = (('link', 'name', 'id'),)
