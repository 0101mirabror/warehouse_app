from rest_framework.views import APIView 
from coreapp.models import *
from django.http import JsonResponse


class ProductAPIView(APIView):
    def get(self, request):
        # requested products and quantity
        req_objs = {key: int(value)  for key, value in request.GET.items()}
        result = []
        # saving remaining data in next loop
        remaining_data = {}
        # loop for each requested object
        for pro_name, pro_qty in  req_objs.items():
            product = Products.objects.get(product_name=pro_name)
            product_materials = ProductMaterials.objects.filter(product_id=product.id)
            # product's all requested materials
            req_obj_mats = {prod_mat.material_id.id: prod_mat.quantity*pro_qty for prod_mat in product_materials}
            obj_data = []
            # loop for each product material
            for mat_id in req_obj_mats.keys():
                warehouses = Warehouses.objects.filter(material_id=mat_id)
                # each product's material quantity 
                mat_taken = req_obj_mats[mat_id]
                c = 0
                for warehouse in warehouses:
                    c+=1
                    # check previous used warehouse 
                    if warehouse.id in remaining_data.keys():
                        warehouse.remainder = remaining_data[warehouse.id]
                        # continue next warehouse if warehouse is empty
                        if remaining_data[warehouse.id] == 0:
                            # execute if all material's warehouses are empty
                            if mat_taken > 0  and len(warehouses) == c:
                                obj_data.append({
                                "warehouse_id": None,
                                "material_name": warehouse.material_id.material_name,
                                "qty": mat_taken,
                                "price": None
                                })
                                break
                            continue
                    # stop loop if product material is already taken
                    if mat_taken == 0:
                        break
                    elif  mat_taken <= warehouse.remainder:
                        obj_data.append({
                                "warehouse_id": warehouse.id,
                                "material_name": warehouse.material_id.material_name,
                                "qty": mat_taken,
                                "price": warehouse.price
                                })
                        remaining_data.update({warehouse.id: warehouse.remainder - mat_taken})
                        mat_taken = 0
                        continue
                    elif mat_taken > warehouse.remainder:
                        obj_data.append({
                                "warehouse_id": warehouse.id,
                                "material_name": warehouse.material_id.material_name,
                                "qty": warehouse.remainder,
                                "price": warehouse.price
                                })
                        mat_taken -= warehouse.remainder
                        # if material is not enough
                        if len(warehouses) == c and mat_taken > 0:
                            obj_data.append({
                                "warehouse_id": None,
                                "material_name": warehouse.material_id.material_name,
                                "qty": mat_taken,
                                "price": None
                                })
                        remaining_data.update({warehouse.id: 0})            
            result.append({
                            'product_name': pro_name,
                            'product_qty': pro_qty,
                            'product_materials': obj_data
                        })
        response_data={"result": result}
        return JsonResponse(response_data)
