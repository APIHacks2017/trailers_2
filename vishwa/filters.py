import itertools

def filter1(list_of_points, type_of_location):

    #print('Inside the filter1 ', list_of_points)
    #print('Inside the filter1 ', type_of_location)
    buffer = []
    for location in list_of_points:
        #print(location, ' Printed')
        if location['type'] in type_of_location:
            buffer.append(location)
    return buffer


def filter2():
    return 'Yet to be done'

def permutations(list_of_points, no_of_points):
    permuted_list = []
    for i in range(0,no_of_points+1):
        for subset in itertools.combinations(list_of_points,i):
            permuted_list.append(list(subset))
    return permuted_list