import json


my_obj = {'name': 'Manik', 'isStudent': True}

with open("data.json", "w") as f:
    my_new_data = json.dump(my_obj, f, indent=4, sort_keys=True)
    
 
    
    