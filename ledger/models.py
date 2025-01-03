from django.db import models
import hashlib


class Blockchain(models.Model):
    data = models.CharField(max_length=255)
    hash = models.CharField(max_length=64)
    prev_hash = models.CharField(max_length=64)


def hashGenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()


class BlockchainManager(models.Manager):
    def create_block(self, data, prev_hash):
        hash_key = hashGenerator(data + prev_hash)
        block = self.model(data=data, hash=hash_key, prev_hash=prev_hash)
        block.save()
        return block