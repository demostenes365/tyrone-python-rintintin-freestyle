def recommend(ice_cream):
  print("you would enjoy:"+ ice_cream)

flavor =input("which ice cream flavor?: vanilla or chocolate:")
toppings =input("do you want toppings?:")
if flavor == "chocolate":
    recommend("nutella")
else:
    recommend("cookies and cream")
if toppings == "yes":
 recommend("choccy balls")
else:
 recommend("none")

