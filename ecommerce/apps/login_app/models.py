from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
	def registerVal(self, postData):
		print postData
		results = {'status': True, 'errors': [], 'user': None}
		if len(postData['first_name']) < 3 and len(postData['first_name']) > 50:
			results['status'] = False
			results['errors'].append('First Name Must be at Least 3 Characters.')
		if len(postData['last_name']) < 3 and len(postData['last_name']) > 50:
			results['status'] = False
			results['errors'].append('Last Name Must be at Least 3 Characters.')
		if len(postData['username']) < 3  and len(postData['first_name']) > 20:
			results['status'] = False
			results['errors'].append('Username Must be at Least 3 Characters.')
		if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
			results['status'] = False
			results['errors'].append('Please Enter a Valid Email.')
		if len(postData['password']) < 4 or postData['password'] != postData['confirm_password']:
			results['status'] = False
			results['errors'].append('Please Enter a Set of Matching Valid Password.')
		if postData["account_type"] == "merchant" and not postData["merchant_code"] == "xxc636":
			results['status'] = False
			results['errors'].append('Please Enter a Valid Merchant Auth Code.')

		user = User.objects.filter(username=postData['username'])
		print user, '*****', len(user)
		if len(user) >= 1:
			results['status'] = False
			results['errors'].append(
			    'User Already Exists, Please Login or Use a Different Username.')
		return results

	def createUser(self, postData):
		p_hash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
		user = User.objects.create(
		    first_name=postData['first_name'], last_name=postData['last_name'], username = postData['username'], email=postData['email'], password=p_hash, account_type = postData['account_type'])
		return user

	def loginVal(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		results['user'] = User.objects.filter(username=postData['username'])
		if len(results['user']) < 1:
			results['status'] = False
			results['errors'].append('Invalid Login Information')
		else:
			hashed = bcrypt.hashpw(postData['password'].encode(
			    ), results['user'][0].password.encode())
			if hashed != results['user'][0].password:
				results['status'] = False
				results['errors'].append('Invalid Login Information')
		return results


class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	username = models.CharField(max_length=20)
	email = models.CharField(max_length=250)
	password = models.CharField(max_length=50)
	account_type = models.CharField(max_length=400)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()
