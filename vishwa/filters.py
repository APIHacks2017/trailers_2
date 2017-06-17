


def filter1(list_of_points, type_of_location):

    #print('Inside the filter1 ', list_of_points)
    #print('Inside the filter1 ', type_of_location)
    buffer = []
    for location in list_of_points:
        #print(location, ' Printed')
        if location['type'] == type_of_location:
            buffer.append(location)
    return buffer


def filter2():
    return 'Yet to be done'