import json


def bio():
    biodata = {
    "name": "Yulianto Wibowo",
    "age": 24,
    "address": "BTN Indogriya E 16, RT03/RW06, Kec. Klangenan, Kab. Cirebon, Jawa Barat - 45156",
    "hobbies": ["desain", "menulis", "koding"],
    "is_married": False,
    "list_school": [
            {
                    "year_in": 2002,
                    "year_out": 2008,
                    "major": "SDN 3 Klangenan"
            },
            {
                    "year_in": 2008,
                    "year_out": 2011,
                    "major": "SMPN 1 Palimanan"
            },
            {
                    "year_in": 2011,
                    "year_out": 2014,
                    "major": "SMAN 1 Palimanan"
            },
    ],
    "skills": [
            {
                    "skill_name": "desain",
                    "level": "advanced",                    
            },
            {
                    "skill_name": "menulis",
                    "level": "expert",                    
            },
            {
                    "skill_name": "koding",
                    "level": "beginner",                    
            }
            
    ],
    "interest_in_coding": True
    
    }
    
    
    with open("biodata.json", "w") as write_file:
        json.dump(biodata, write_file)
    json_biodata = json.dumps(biodata)
    
bio()