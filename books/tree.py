from os import listdir
from os.path import isfile, join
from collections import deque

def print_names(root):
    search_deque = deque()
    search_deque.append(root)
    while search_deque:
        dir = search_deque.popleft()
        for file in sorted(listdir(dir)):
            full_path = join(dir, file)
            if isfile(full_path):
                print(file)
            else:
                search_deque.append(full_path)
print_names("pics")

# def print_name(root):
#     for file in sorted(listdir(root)):
#         path = join(root, file)
#         if isfile(path):
#             print(file)
#         else:
#             print_name(path)
# print_name('pics')
