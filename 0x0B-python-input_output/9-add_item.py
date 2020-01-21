#!/usr/bin/python3

from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

'''
Write a script that adds all
arguments to a Python list, and then
save them to a file
'''


argc = len(argv)
filename = 'add_item.json'
with open(filename, 'r', encoding='utf-8') as f:
    count = 0
    for line in f:
        count += 1
if count > 0:
    my_list = []
    my_list = load_from_json_file(filename)
else:
    my_list = []
for items in range(1, argc):
    my_list.append(argv[items])

save_to_json_file(my_list, filename)
