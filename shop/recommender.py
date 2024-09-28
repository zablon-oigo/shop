import redis
from django.conf import settings
from .models import Product


r=redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT,db=settings.REDIS_DB)

class Recommender:
    def get_product_key(self,id):
        return f'product:{id}:purchased_with'