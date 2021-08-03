def run ():
    my_list = [1, 'hello', 4, 4,5]
    my_dicc = {'firstname':'bruno', 'lastname': 'monte'} 

    super_list = [
        {'firstname':'bruno', 'lastname': 'monte'},
        {'firstname':'santi', 'lastname': 'gior'},
        {'firstname':'lucio', 'lastname': 'dav'},
        {'firstname':'pepe', 'lastname': 'ships'},
        {'firstname':'marcos', 'lastname': 'balbi'},
    ]

    super_dicc = {
        'natural_nums':[3,5,3,5,6,9],
        'integer_nums' : [-5,-6,0,8,7],
        'floating_nums' : [1.2,8.6,9.7]
    }

    for key, value in super_dicc.items():
        print(key, '-', value)
    
    for i in super_list:
        for key, values in i.items():
            print(key,": ", values)
            
if __name__ == '__main__':
    run()