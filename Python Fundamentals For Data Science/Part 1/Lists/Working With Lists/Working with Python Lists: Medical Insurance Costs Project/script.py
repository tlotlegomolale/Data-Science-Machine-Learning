names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append("Priscilla")
insurance_costs.append(8320.0)

medical_records = list(zip(insurance_costs, names))
print(medical_records)

num_medical_records = len(medical_records)
print("There are " + str(num_medical_records) + " medical records.")

first_medical_record = medical_records[0]
print("Here is he first medical record: "+ str(first_medical_record)) 

medical_records.sort()
print("Here are the medical records sorted by insurance cost: " + str(medical_records))

cheapest_three = medical_records[:3]
print("Here are the three cheapest insurance costs in our records: " + str(cheapest_three))

priciest_three = medical_records[-3:]
print("here are the three most expensive insurance costs in our medical records: " + str(priciest_three))

occurrences_paul = names.count("Paul")
print("There are " + str(occurrences_paul) + " individuals with the name Paul in our medical records.")

# Extra
sorted_by_name = list(zip(names, insurance_costs))
sorted_by_name.sort()
print(sorted_by_name)

middle_five_records = sorted_by_name[3:8]
print(middle_five_records)
