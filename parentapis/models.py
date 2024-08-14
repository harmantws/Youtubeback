from django.db import models
import uuid
from authentication.models import CustomUser
# Create your models here.
class SearchHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    query = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class NotAllowedSearches(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    searches = models.TextField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)