# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(age,sex,bmi,num_of_children,smoker,name):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for " + name + " is {0} dollars.".format(estimated_cost))
  return estimated_cost


# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(28,0,26.2,3,0,"maria")



# Initial variables for Omar
age = 35
sex = 1 
bmi = 22.2
num_of_children = 0
smoker = 1  

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost(35,1,22.2,0,1,"omar")


#My insurance cost

my_insurance_cost = calculate_insurance_cost(25,1,27,0,1,"Lethabo")
