import json

# 本月企業愛用人資證照的排名資料
this_month_rankings = {
    "Comprehensive Basic Human Resources Management Certification",
    "Labor Laws & Regulations Certification Program",  # 修改此處表述方式
    "Labor Insurance, Health Insurance, and Labor Standards Act Management Certification",  # 修改此處表述方式
    "Human Resources Project Management Certification",
    "Employee Compensation Management Certification",
    "Strategic Human Resources Management Certification"
}

# 人資常見證照資料
common_certifications = {
    "Level B technician for Employment Service",
    "Fundamental Human Resource Management Certification",
    "Labor Laws & Regulations Certification Program",
    "Labor Insurance, Health Insurance and Labor Standards Act Management Certification",
    "Strategic Human Resource Management Certification",
    "Compensation Administration Certification Program",
    "Training and Development Manager Certification",
    "HR Project Management Professional Certification Program",
    "Human Resources and Compensation Manager Certification",
    "Innovation of Human Resources Management"
}

# 交集：找出兩組資料共同擁有的證照名稱
intersection = this_month_rankings.intersection(common_certifications)

# 輸出交集的證照名稱
print("交集：")
for cert in intersection:
    print(cert)





#找出起薪（less than 1 year）最高的產業類別
data = {
    "Electronics/Information Technology/Software/Semiconductors": 35000,
    "General Traditional Manufacturing": 32000,
    "Politics/Religion/Social Welfare": 34000,
    "Finance/Investment/Insurance Related": 31000,
    "Legal/Accounting/Consulting/R&D/Design": 33851,
    "Transportation/Logistics/Warehousing": 32000,
    "Construction/Real Estate Related": 34500,
    "Medical Care/Environmental Health": 33000,
    "Agriculture/Forestry/Fisheries/Hydro Resources": 32900,
    "General Service Industry": 32000,
    "Tourism/Leisure/Sports": 33000,
    "Food/Beverage/Accommodation Services": 32000,
    "Mass Communication Related": 32000,
    "Education/Publishing/Arts Related": 33000,
    "Wholesale/Retail": 33000
}

sorted_data = sorted(data, key=data.get, reverse=True)

print("Less than 1 year salary 的產業名稱（Industry）：")
for industry in sorted_data:
    print(industry)




#找出more than 7 years 和 less than 1 year salary的相差值最高的產業並算出相差值為何
data = {
    "Electronics/Information Technology/Software/Semiconductors": {"Less than 1 year salary": 35000, "More than 7 years salary": 40100},
    "General Traditional Manufacturing": {"Less than 1 year salary": 32000, "More than 7 years salary": 36500},
    "Politics/Religion/Social Welfare": {"Less than 1 year salary": 34000, "More than 7 years salary": 41500},
    "Finance/Investment/Insurance Related": {"Less than 1 year salary": 31000, "More than 7 years salary": 50000},
    "Legal/Accounting/Consulting/R&D/Design": {"Less than 1 year salary": 33851, "More than 7 years salary": 50000},
    "Transportation/Logistics/Warehousing": {"Less than 1 year salary": 32000, "More than 7 years salary": 43000},
    "Construction/Real Estate Related": {"Less than 1 year salary": 34500, "More than 7 years salary": 39500},
    "Medical Care/Environmental Health": {"Less than 1 year salary": 33000, "More than 7 years salary": 36700},
    "Agriculture/Forestry/Fisheries/Hydro Resources": {"Less than 1 year salary": 32900, "More than 7 years salary": 41500},
    "General Service Industry": {"Less than 1 year salary": 32000, "More than 7 years salary": 42000},
    "Tourism/Leisure/Sports": {"Less than 1 year salary": 33000, "More than 7 years salary": 35600},
    "Food/Beverage/Accommodation Services": {"Less than 1 year salary": 32000, "More than 7 years salary": 36100},
    "Mass Communication Related": {"Less than 1 year salary": 32000, "More than 7 years salary": 42500},
    "Education/Publishing/Arts Related": {"Less than 1 year salary": 33000, "More than 7 years salary": 38000},
    "Wholesale/Retail": {"Less than 1 year salary": 33000, "More than 7 years salary": 40000}
}

max_difference = 0
max_difference_industry = ""

print("各產業 Less than 1 year salary 和 More than 7 years salary 的薪資差值：")
for industry, salaries in data.items():
    less_than_1_year_salary = salaries["Less than 1 year salary"]
    more_than_7_years_salary = salaries["More than 7 years salary"]
    difference = more_than_7_years_salary - less_than_1_year_salary
    print(f"{industry}: {difference}")

    if difference > max_difference:
        max_difference = difference
        max_difference_industry = industry

print(f"\n薪資差值最大的產業：{max_difference_industry}，差值為 {max_difference}")
