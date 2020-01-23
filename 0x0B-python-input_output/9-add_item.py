#!/usr/bin/python3
import json
import sys
import os
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


list_1 = []

if not os.path.exists("./add_item.json"):
    save_to_json_file(list_1, "add_item.json")

my_list = load_from_json_file("add_item.json")

for i in sys.argv[1:]:
    list_1.append(i)

save_to_json_file(list_1, "add_item.json")
