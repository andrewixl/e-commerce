from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User
from datetime import datetime
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class ProductManager(models.Manager):
    def createProduct(self, postData, user_id):
        results = {'status': True, 'errors': [], 'user': None}
        if len(postData['product_name']) < 3:
			results['status'] = False
			results['errors'].append('Product Name Must be at Least 3 Characters.')
        if len(postData['price']) < 1:
			results['status'] = False
			results['errors'].append('Please Enter a Valid Price.')
        if len(postData['weight']) < 1:
			results['status'] = False
			results['errors'].append('Please Enter a Valid Weight in Pounds.')
        if len(postData['description']) < 10:
			results['status'] = False
			results['errors'].append('Description Must be at Least 10 Characters.')
        url = URLValidator()
        try:
            url(postData['image_link'])
        except:
            results['status'] = False
            results['errors'].append('Please Enter Proper Url such as http://google.com')

        if results['status'] == True:
            userInt = int(user_id)
            user = User.objects.get(id=userInt)
            results['product'] = Product.objects.create(product_name=postData['product_name'], price=postData['price'], weight=postData['weight'], image_link=postData['image_link'], description=postData['description'], views=0, seller=user)
        return results


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    weight = models.FloatField()
    image_link = models.URLField(max_length=500, default="http://polyureashop.studio.crasman.fi/pub/web/img/no-image.jpg")
    description = models.CharField(max_length=500)
    views = models.IntegerField()
    seller = models.ForeignKey('login_app.User')
    purchaser = models.ManyToManyField('login_app.User', related_name="purchaser")
    reviews = models.ManyToManyField('login_app.User', related_name="reviews")
    cart = models.ManyToManyField('login_app.User', related_name="carted")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()

class ReviewManager(models.Manager):
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


class Review(models.Model):
    review_title = models.CharField(max_length=100)
    rating = models.IntegerField()
    description = models.CharField(max_length=500)
    owner = models.ForeignKey('login_app.User')
    product = models.ManyToManyField('Product', related_name="product")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
