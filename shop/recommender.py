import redis
from django.conf import settings
from .models import Product


r=redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT,db=settings.REDIS_DB)

class Recommender:
    def get_product_key(self,id):
        return f'product:{id}:purchased_with'
    def products_bought(self, products):
        product_ids=[p.id for p in products]
        for product_id in product_ids:
            for with_id in product_ids:
                if product_id != with_id:
                    r.zincrby(self.get_product_key(product_id), 1, with_id)