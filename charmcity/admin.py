from django.contrib import admin
from .models import Cart,Category,Sub_category,Product,Order




class CategoryAdmin(admin.ModelAdmin):
        list_display = ['id', 'name']
        
class Sub_categoryAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'name' , 'category']
    
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'description', 'brand' , 'weight' , 'size', 'price' , 'category' , 'sub_category' , 'sale']
    
    
class CartAdmin(admin.ModelAdmin):
    list_display = [ 'id' , 'product' , 'user' , 'quantity' ,'sub_total']
    
    
    
class OrderAdmin(admin.ModelAdmin):
    list_display = [ 'id' , 'first_name' , 'last_name' , 'address' , 'city' , 'phone' , 'postal' , 'is_delivered']
    
    
    
admin.site.register(Category,CategoryAdmin)   
admin.site.register(Sub_category,Sub_categoryAdmin)   
admin.site.register(Product,ProductAdmin)   
admin.site.register(Cart,CartAdmin)   
admin.site.register(Order,OrderAdmin)

   
             