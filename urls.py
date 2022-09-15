from django.contrib import admin
from django.urls import path

from newapp.views import ec2, iamss, vpcd, lambb, sns1, rds1, ebs1, ss1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ec2des', ec2.as_view()),
    path('iam', iamss.as_view()),
    path('vpc', vpcd.as_view()),
    path('lambdda', lambb.as_view()),
    path('sns', sns1.as_view()),
    path('rds', rds1.as_view()),
    path('ebs', ebs1.as_view()),
    path('s3', ss1.as_view())
]
