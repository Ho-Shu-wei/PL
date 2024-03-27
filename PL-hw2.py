import json

data = {
    "Electronics/Information Technology/Software/Semiconductors": {
        "Less than 1 year salary": 35000,
        "1-3 years salary": 37500,
        "3-5 years salary": 38500,
        "5-7 years salary": 39000,
        "More than 7 years salary": 40100
    },
    "General Traditional Manufacturing": {
        "Less than 1 year salary": 32000,
        "1-3 years salary": 32500,
        "3-5 years salary": 35000,
        "5-7 years salary": 36100,
        "More than 7 years salary": 36500
    },
    "Politics/Religion/Social Welfare": {
        "Less than 1 year salary": 34000,
        "1-3 years salary": 34600,
        "3-5 years salary": 35656,
        "5-7 years salary": 38000,
        "More than 7 years salary": 41500
    },
    "Finance/Investment/Insurance Related": {
        "Less than 1 year salary": 31000,
        "1-3 years salary": 31300,
        "3-5 years salary": 36000,
        "5-7 years salary": 40500,
        "More than 7 years salary": 50000
    },
    "Legal/Accounting/Consulting/R&D/Design": {
        "Less than 1 year salary": 33851,
        "1-3 years salary": 34500,
        "3-5 years salary": 40000,
        "5-7 years salary": 41750,
        "More than 7 years salary": 50000
    },
    "Transportation/Logistics/Warehousing": {
        "Less than 1 year salary": 32000,
        "1-3 years salary": 32400,
        "3-5 years salary": 33300,
        "5-7 years salary": 34000,
        "More than 7 years salary": 43000
    },
    "Construction/Real Estate Related": {
        "Less than 1 year salary": 34500,
        "1-3 years salary": 35600,
        "3-5 years salary": 38000,
        "5-7 years salary": 38500,
        "More than 7 years salary": 39500
    },
    "Medical Care/Environmental Health": {
        "Less than 1 year salary": 33000,
        "1-3 years salary": 34200,
        "3-5 years salary": 35000,
        "5-7 years salary": 35800,
        "More than 7 years salary": 36700
    },
    "Agriculture/Forestry/Fisheries/Hydro Resources": {
        "Less than 1 year salary": 32900,
        "1-3 years salary": 33200,
        "3-5 years salary": 36000,
        "5-7 years salary": 37500,
        "More than 7 years salary": 41500
    },
    "General Service Industry": {
        "Less than 1 year salary": 32000,
        "1-3 years salary": 32500,
        "3-5 years salary": 33000,
        "5-7 years salary": 35000,
        "More than 7 years salary": 42000
    },
    "Tourism/Leisure/Sports": {
        "Less than 1 year salary": 33000,
        "1-3 years salary": 33200,
        "3-5 years salary": 33500,
        "5-7 years salary": 34000,
        "More than 7 years salary": 35600
    },
    "Food/Beverage/Accommodation Services": {
        "Less than 1 year salary": 32000,
        "1-3 years salary": 33200,
        "3-5 years salary": 34000,
        "5-7 years salary": 35000,
        "More than 7 years salary": 36100
    },
    "Mass Communication Related": {
        "Less than 1 year salary": 32000,
        "1-3 years salary": 33000,
        "3-5 years salary": 34100,
        "5-7 years salary": 42100,
        "More than 7 years salary": 42500
    },
    "Education/Publishing/Arts Related": {
        "Less than 1 year salary": 33000,
        "1-3 years salary": 33600,
        "3-5 years salary": 34000,
        "5-7 years salary": 35600,
        "More than 7 years salary": 38000
    },
    "Wholesale/Retail": {
        "Less than 1 year salary": 33000,
        "1-3 years salary": 33600,
        "3-5 years salary": 35000,
        "5-7 years salary": 37000,
        "More than 7 years salary": 40000
    }
}

# Convert data to JSON format
json_data = json.dumps(data, ensure_ascii=False, indent=4)

# Write JSON data to a file
with open("salary_data.json", "w") as json_file:
    json_file.write(json_data)

print("JSON data has been saved to 'salary_data.json'")




# Rankings data
rankings = [
    "Comprehensive Basic Human Resources Management Certification",
    "Labor Law and Regulations Management Certification",
    "Labor Insurance, Health Insurance, and Labor Standards Act Management Certification",
    "Human Resources Project Management Certification",
    "Employee Compensation Management Certification",
    "Strategic Human Resources Management Certification"
]

# Convert the rankings data to JSON format
json_data = {"Monthly Preferred Certifications by Enterprises": rankings}

# Output JSON data to a file
with open('rankings.json', 'w') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=4)

print("JSON file generated successfully!")




data = {
    "1": "Level B technician for Employment Service",
    "2": "Fundamental Human Resource Management Certification",
    "3": "Labor Laws & Regulations Certification Program",
    "4": "Labor Insurance, Health Insurance and Labor Standards Act Management Certification",
    "5": "Strategic Human Resource Management Certification",
    "6": "Compensation Administration Certification Program",
    "7": "Training and Development Manager Certification",
    "8": "HR Project Management Professional Certification Program",
    "9": "HR Project Management Professional Certification Program",
    "10": "Human Resources and Compensation Manager Certification",
    "11": "Innovation of Human Resources Management"
}

# Convert data to JSON
json_data = json.dumps(data, ensure_ascii=False, indent=4)

# Write JSON data to a file
with open("hr_certifications.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_data)

print("Data has been successfully converted to JSON and saved to 'hr_certifications.json' file.")








