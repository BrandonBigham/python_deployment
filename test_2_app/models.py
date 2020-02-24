from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, requestPOST):
        errors = {}
        if len(requestPOST['first_name']) < 3:
            errors['first_name'] = "Name is too short"
        if len(requestPOST['last_name']) < 1:
            errors['last_name'] = "must have a last name"
        if len(requestPOST['email']) < 8:
            errors['email'] = "must have a valid email"
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(requestPOST['email']):
            errors['invalid_email'] = "must have a valid email"
        # users_with_name = User.objects.filter(name=requestPOST['name'])
        # if len(users_with_name) > 0:
        #     errors['duplicate_name'] = "Name already taken" SEE LINE 40
        users_with_email = User.objects.filter(email=requestPOST['email'])
        if len(users_with_email) > 0:
            errors['duplicate_email'] = "email is already taken"
        if len(requestPOST['password']) < 8:
            errors['password'] = "Password is too short"
        if requestPOST['password'] != requestPOST['password_conf']:
            errors['no_match'] = "Password and Password Confirmation must match"
        return errors
    def edit_validator(self, requestPOST):
        errors = {}
        if len(requestPOST['first_name']) < 3:
            errors['first_name'] = "Name is too short"
        if len(requestPOST['last_name']) < 1:
            errors['last_name'] = "must have a last name"
        if len(requestPOST['email']) < 8:
            errors['email'] = "must have a valid email"
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(requestPOST['email']):
            errors['invalid_email'] = "must have a valid email"
        # users_with_name = User.objects.filter(name=requestPOST['name'])
        # if len(users_with_name) > 0:
        #     errors['duplicate_name'] = "Name already taken" whoops. already migrated so im scared to delete it lol
        users_with_email = User.objects.filter(email=requestPOST['email'])
        if len(users_with_email) > 0:
            errors['duplicate_email'] = "email is already taken"
        return errors
        

class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    password = models.TextField()
    email = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class PostManager(models.Manager):
    def post_validator(self, requestPOST):
        errors = {}
        if len(requestPOST['quote']) < 10:
            errors['quote'] = "Quote is too short"
        if len(requestPOST['author']) < 3:
            errors['author'] = "Author name is too short"
        return errors

class Post(models.Model):
    quote = models.TextField()
    owner = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    author = models.TextField()
    likes = models.ManyToManyField(User, related_name="cats_voted_for")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()
