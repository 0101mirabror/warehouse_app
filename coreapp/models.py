from django.db import models

class Materials(models.Model):
    class Meta:
        verbose_name_plural = "Xomashyolar"

    material_name = models.CharField(max_length=30)

    def __str__(self):
        return self.material_name


class Products(models.Model):
    class Meta:
        verbose_name_plural = "Mahsulotlar"

    product_name = models.CharField(max_length=30)
    product_code = models.CharField(max_length=20)

    def __str__(self):
        return self.product_name


class ProductMaterials(models.Model):
    class Meta:
        verbose_name_plural = "Mahsulot-Xomashyolar"

    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    material_id = models.ForeignKey(Materials, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return str(self.product_id) + " — " + str(self.material_id)

    
    

class Warehouses(models.Model):
    class Meta:
        verbose_name_plural = "Omborxonalar"
    material_id = models.ForeignKey(Materials, on_delete=models.CASCADE)
    remainder = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.material_id)
