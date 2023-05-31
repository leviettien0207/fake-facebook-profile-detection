import os

def new_file():
    i = 0
    while os.path.isfile('out\\result_{}'.format(i)):
        i += 1
    
    return 'out\\result_{}'.format(i)

def new_file_2():
    i = 0
    while os.path.isfile('out_2\\result_{}.json'.format(i)):
        i += 1
    
    return 'out_2\\result_{}.json'.format(i)




