def run():
   # sqares = []
   # for i in range (1,101):
   #     if (i % 3 != 0 ):
   #         sqares.append(i **2)

    #sqares = [i**2 for i in range (1,101) if i % 3 != 0] 
    multiplos_de_cuatro = [i*4 for i in range(1,100000) if (i*4 % 6 == 0 and i*4 % 9 ==0)]
    
    print(multiplos_de_cuatro)
if __name__ == '__main__':
    run()