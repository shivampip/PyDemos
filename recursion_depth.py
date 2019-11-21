

count= 1

def d():
    global count
    count+= 1
    d()


try:
    d()
except RecursionError as re:
    print("Recursion depth: {}".format(count))