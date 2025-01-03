from django.contrib import admin
from ledger.models import Blockchain, BlockchainManager
# Register your models here.
admin.site.register(Blockchain)
#admin.site.register(BlockchainManager)