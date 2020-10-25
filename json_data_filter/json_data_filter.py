import os
import json
from datetime import datetime

# get all json files from current directory
dir_content = os.listdir(".")
json_files = [doc for doc in dir_content if doc.endswith("json")]
processed = 0

# get a file reference to write data to (summary.csv)
data_file = open("./summary.csv", "w")
data_file.write("username, email, cell, name, age, full address, dob, pob, registration date\n")

for doc in json_files:

    #open the json file and load the content into a dictionary
    with open(doc, "r") as json_file:

        try:
            content = json.loads(json_file.read())
            
            username = content["login"]["username"]
            name = content["name"]["title"] + content["name"]["first"] + " " + content["name"]["last"]
            age = content["dob"]["age"]
            dob = datetime.strptime(content["dob"]["date"], '%Y-%m-%dT%H:%M:%SZ')
            email = content["email"]
            cell = content["cell"]
            address = content["location"]["street"]
            city = content["location"]["city"]
            state = content["location"]["state"]
            full_address = f"{address} - {city} - {state}"
            pob = content["nat"]
            registration_date = datetime.strptime(content["registered"]["date"], '%Y-%m-%dT%H:%M:%SZ')
            # write data to file
            data_file.write(f"{username}, {email}, {cell}, {name}, {age}, {full_address}, {dob}, {pob}, {registration_date}\n")

            processed+=1

            print(f"{username}: {email}, {cell}, {name}, {age}, {full_address}, {dob}, {pob}, {registration_date}")
        except json.decoder.JSONDecodeError as err:
            print(f"Could not load json from {doc}... {err}")

print(f"Processed {processed} of {len(json_files)}")

        
