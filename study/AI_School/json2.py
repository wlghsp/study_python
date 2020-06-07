import json

student_data = {
    "1.FirstName": "JaeHwa",
    "2.LastName": "Lee",
    "3.Age": 20,
    "4.Youtube_ch": "AIRIM",
    "5.Courses": [
        {
            "Major_A": "ML",
            "Classes": ["Probability",
                        "Generalized Linear Model",
                        "Categorical Data Analysis"]
        },
        {
            "Major_B": "Deep Learning",
            "Classes": ["Data Structure",
                        "Programming",
                        "Algorithms"]
        }
    ]
}

st_json = json.dumps(student_data, indent=4)

print(st_json)