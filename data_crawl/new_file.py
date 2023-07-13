import os


def new_file():
    i = 0
    while os.path.isfile('out\\result_{}'.format(i)):
        i += 1

    return 'out\\result_{}'.format(i)


def new_file_2():
    i = 0
    while os.path.isfile('out_data\\result_{}.json'.format(i)):
        i += 1

    return 'out_data\\result_{}.json'.format(i)


def new_file_3():
    i = 0
    while os.path.isfile('out_3\\result_{}.json'.format(i)):
        i += 1

    return 'out_3\\result_{}.json'.format(i)
