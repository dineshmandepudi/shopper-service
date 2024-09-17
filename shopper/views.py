import csv
import json
import os

from django.http.response import JsonResponse


from db_data.models import StoreData
from django.conf import settings


def return_json(reqeust):
    """Read the file content from DB and Return the JSON response"""
    file_inst = StoreData.objects.first()
    file_path = file_inst.file_name
    final_list = list()
    complete_file_path = os.path.join(settings.BASE_DIR, file_path)

    with open(complete_file_path) as file_obj:
        complete_data = csv.DictReader(file_obj, delimiter=',', quotechar='"')
        for each_row in complete_data:
            final_list.append(each_row)

    return JsonResponse({"shopper_data_address": final_list})


    # final_list = list()
    # file_name = "shopper-data-address.csv"
    # complete_path = os.path.join(os.getcwd(), file_name)
    #
    # with open(complete_path) as file_obj:
    #     complete_data = csv.DictReader(file_obj, delimiter=',', quotechar='"')
    #     for each_row in complete_data:
    #         final_list.append(each_row)
    #
    # return JsonResponse({"shopper_data_address": final_list})
