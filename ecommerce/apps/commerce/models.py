from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User
from datetime import datetime

class PlanManager(models.Manager):
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


class Plan(models.Model):
    destination = models.CharField(max_length=100)
    travelstartdate = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now())
    travelenddate = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now())
    description = models.CharField(max_length=250)
    owner = models.ForeignKey('login_app.User')
    joiners = models.ManyToManyField('login_app.User', related_name="joiners")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PlanManager()
