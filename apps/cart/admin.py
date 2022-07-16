from django.contrib import admin


# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product',
                    'quantity',
                    'price_ht',
                    'cart',
                    ]


# admin.site.register(
#     CartAdmin,
#     CartItemAdmin
#     )
