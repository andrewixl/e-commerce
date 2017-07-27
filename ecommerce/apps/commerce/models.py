from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User
from datetime import datetime

class ProductManager(models.Manager):
    def createPlan(self, postData, user_id):
        results = {'status': True, 'errors': [], 'user': None}
        if len(postData['destination']) < 3:
			results['status'] = False
			results['errors'].append('Destination Name Must be at Least 3 Characters.')
        if len(postData['description']) < 10:
			results['status'] = False
			results['errors'].append('Description Must be at Least 10 Characters.')
        if postData['travelstartdate'] > postData['travelenddate'] or str(postData["travelstartdate"]) < str(datetime.now().date()):
			results['status'] = False
			results['errors'].append('End Date Must Be After Start Date and Future Dated.')
        # if len(postData['travelenddate']) < 1:
		# 	results['status'] = False
		# 	results['errors'].append('Description Must be at Least 10 Characters.')

        if results['status'] == True:
            userInt = int(user_id)
            user = User.objects.get(id=userInt)
            results['plan'] = Plan.objects.create(destination=postData['destination'], description=postData['description'], travelstartdate=postData['travelstartdate'], travelenddate=postData['travelenddate'], owner=user)
        return results


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    weight = models.IntegerField()
    description = models.CharField(max_length=500)
    seller = models.ForeignKey('login_app.User')
    reviews = models.ManyToManyField('login_app.User', related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()

class ReviewsManager(models.Manager):
    def createPlan(self, postData, user_id):
        results = {'status': True, 'errors': [], 'user': None}
        if len(postData['destination']) < 3:
			results['status'] = False
			results['errors'].append('Destination Name Must be at Least 3 Characters.')
        if len(postData['description']) < 10:
			results['status'] = False
			results['errors'].append('Description Must be at Least 10 Characters.')
        if postData['travelstartdate'] > postData['travelenddate'] or str(postData["travelstartdate"]) < str(datetime.now().date()):
			results['status'] = False
			results['errors'].append('End Date Must Be After Start Date and Future Dated.')
        # if len(postData['travelenddate']) < 1:
		# 	results['status'] = False
		# 	results['errors'].append('Description Must be at Least 10 Characters.')

        if results['status'] == True:
            userInt = int(user_id)
            user = User.objects.get(id=userInt)
            results['plan'] = Plan.objects.create(destination=postData['destination'], description=postData['description'], travelstartdate=postData['travelstartdate'], travelenddate=postData['travelenddate'], owner=user)
        return results


class Reviews(models.Model):
    review_title = models.CharField(max_length=100)
    rating = models.IntegerField()
    description = models.CharField(max_length=500)
    owner = models.ForeignKey('login_app.User')
    product = models.ManyToManyField('Product', related_name="product")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
