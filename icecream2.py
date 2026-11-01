def recommend(ice_cream):
  print("you would enjoy:"+ ice_cream)

flavor =input("which ice cream flavor?: vanilla or chocolate(or strawberry):")
toppings =input("do you want toppings?:")
if flavor == "chocolate":
    recommend("nutella")
if flavor == "vanilla":
     recommend("cookies and cream")
if flavor == "strawberry":
    recommend("berries")
else:
 print("thats not a real flavor")
if toppings == "yes":
 recommend("choccy balls")
if toppings =="no":
 recommend("none")
else:
    print("whuh what")

 

