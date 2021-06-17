import json
print("vnr clg")
print("name :: Akash reddy")
dictionary ={
"name" : "sathiyajith",
"rollno" : 56,
"cgpa" : 8.6,
"phonenumber" : "9976770500"
}
json_object = json.dumps(dictionary, indent = 4)
