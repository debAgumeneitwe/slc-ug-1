""""print ("Get the ingredients")
print ("mix")
print ("pour into heated pan")
print ("flip the egg to the other side")
breakfast = "-------yummy egg------"
print (breakfast)


print ("Get the ingredients")
print ("mix")
print ("pour into heated pan")
print ("flip the egg to the other side")
breakfast = "-------yummy pancake------"
print (breakfast)"""

"""def breakfast(food,ingredients):
    #ingredients = []
    #food = input("what type of breakfast will you have? ",food)
    print ("Get the ingredients")
    #ingredients = input("ingredients include ")
    print ("mix")
    print ("pour into heated pan")
    print ("flip the egg to the other side")
    breakfast = "-------yummy"+ food + "------"  
    return breakfast"""

#print (breakfast("egg"))
#print (breakfast("pancake"))

ingredients = ["bacon","tomatoes"]
def mix_and_cook(food):
    print ("Get the ingredients")
    print ("mix")
    print ("pour into heated pan")
    print ("flip the {} to the other side".format(food))
    #breakfast = "-------yummy pancake served with" + ""------"
    
def breakfast(food,ingredients):
    mix_and_cook(food)
    if len(ingredients) == 0:
        print ("yummy {}".format(food))
        
    else:
        print ("yummy " + food +  " served with " + ",".join(ingredients) )
        
breakfast("eggs",ingredients)
        
         
    
    