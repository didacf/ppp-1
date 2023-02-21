# Hello Function
def hello(name):
    print(f"Hello {name} I hope you are doing well")
hello("Didac")

#pack function with the arguments:

def pack(arg1, arg2, arg3):
    print(arg1, arg2, arg3)
pack("Audi","Bugatti", "Porsche")

#eat_lunch function with any length, range and conditional statements:

def eat_lunch(my_lunch):
   if len(my_lunch) == 0:
       print("My lunchbox is empty!")
   else:
       for i in range(len(my_lunch)):    
         if i == 0:
             print(f"First I eat {my_lunch[0]}")
         else:
             print(f"Next I eat {my_lunch[i]}")

eat_lunch([])
eat_lunch(["carpaccio"])
eat_lunch(["calamari", "filet mignon", "lobster", "pears"])
                 