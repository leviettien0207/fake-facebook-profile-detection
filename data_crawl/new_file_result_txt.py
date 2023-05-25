import os

def new_file():
    i = 0
    while os.path.isfile('out\\result_{}'.format(i)):
        i += 1
    
    return 'out\\result_{}'.format(i)




