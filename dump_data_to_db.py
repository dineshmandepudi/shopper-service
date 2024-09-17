import csv
import os

import psycopg2


def dump_data_to_db():
    """
    Add file name and file path in DB
    :return: None
    """
    file_name = "shopper-data-address.csv"
    complete_path = os.path.join(os.getcwd(), file_name)

    # final_list = list()
    #
    # with open(complete_path) as file_obj:
    #     complete_data = csv.DictReader(file_obj, delimiter=',', quotechar='"')
    #     for each_row in complete_data:
    #         final_list.append(each_row)

    with psycopg2.connect("postgresql://postgres:test123@localhost/postgres") as conn:
        with conn.cursor() as cursor:
            query_string = f"insert into "\
                           f"db_data_storedata(file_content, file_name) "\
                           f"values('{file_name}','{file_name}')"
            cursor.execute(query_string)

        conn.commit()

    print("updated DB")


if __name__ == "__main__":
    dump_data_to_db()



# def read_file(file_name):
#     final_list = list()
#
#     with open(file_name) as file_obj:
#         complete_data = csv.DictReader(file_obj, delimiter=',', quotechar='"')
#         for each_row in complete_data:
#             final_list.append(each_row)
#
#     return json.dumps({"shopper_data_address": final_list})


# if __name__ == "__main__":
#     file_name = "shopper-data-address.csv"
#     complete_path = os.path.join(os.getcwd(), file_name)
#     json_output = read_file(complete_path)
#     print(json_output)
#


