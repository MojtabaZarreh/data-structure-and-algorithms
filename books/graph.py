from collections import deque

graph = {}

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# print(search_queue)

def per_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set()
    while search_queue:
        per = search_queue.popleft()
        if per not in searched:
            if per_is_seller(per) :
                print(f'{per} is a mango saller !!!')
                return True
        else:
            search_queue += graph[per]
            searched.append(per)
    return False

search("claire")   