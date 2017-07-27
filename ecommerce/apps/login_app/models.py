from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

# Create your models here.


class UserManager(models.Manager):
	def registerVal(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		if len(postData['first_name']) < 3:
			results['status'] = False
			results['errors'].append('First Name Must be at Least 3 Characters.')
		if len(postData['last_name']) < 3:
			results['status'] = False
			results['errors'].append('Last Name Must be at Least 3 Characters.')
		if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
			results['status'] = False
			results['errors'].append('Please Enter a Valid Email.')
		if len(postData['password']) < 4 or postData['password'] != postData['confirm_password']:
			results['status'] = False
			results['errors'].append('Please Enter a Set of Matching Valid Password.')

		user = User.objects.filter(email=postData['email'])
		print user, '*****', len(user)
		if len(user) >= 1:
			results['status'] = False
			results['errors'].append(
			    'User Already Exists, Please Login or Use New Email.')
		return results

	def createUser(self, postData):
		p_hash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
		user = User.objects.create(
		    first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=p_hash)
		return user

	def loginVal(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		results['user'] = User.objects.filter(email=postData['email'])
		if len(results['user']) < 1:
			results['status'] = False
			results['errors'].append('Something Went Wrong.')
		else:
			hashed = bcrypt.hashpw(postData['password'].encode(
			    ), results['user'][0].password.encode())
			if hashed != results['user'][0].password:
				results['status'] = False
				results['errors'].append('Something Went Wrong.')
		return results


class User(models.Model):
	first_name = models.CharField(max_length=400)
	last_name = models.CharField(max_length=400)
	email = models.CharField(max_length=400)
	password = models.CharField(max_length=400)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()
