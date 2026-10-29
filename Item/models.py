from django.db import models

# Create your models here.

REPORT_TYPE_CHOICES = [
    ('LOST','Lost'),('FOUND', 'Found')
]
CATEGORY_CHOICES = [
    ('ELECTRONICS', 'Electronics'),
    ('ACCESSORIES','Accessories'),
    ('BAGS_WALLET', 'Bags & Wallet'),
    ('DOCUMENT & ID', 'Documents & ID'),
    ('BOOKS_STATIONARY','Books & Stationery'),
    ('CLOTHING','Clothing'),
    ('KEYS','Keys'),
    ('OTHER', 'Other')
]
STATUS_CHOICES = [
    ('ACTIVE', 'Active'),
    ('CLAIM_PENDING', 'Claim Pending'),
    ('RETURNED', 'Returned'),
    ('CLOSED', 'Closed'),
]
class ItemReport(models.Model):
    title = models.CharField(max_length=100)
    report_type = models.CharField(max_length=5 , choices=REPORT_TYPE_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    location = models.CharField(max_length=100)
    status = models.CharField( max_length=50, choices=STATUS_CHOICES, default='ACTIVE')
    created_at = models.DateTimeField(auto_now_add=True)
