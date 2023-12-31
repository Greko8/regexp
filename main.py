from pprint import pprint
import csv
import re

with open("data/phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pattern = r"(^\w+)[\s|,]?(\w+)[\s|,]?(\w+)?,{1,3}(\w*),([^,]*),((\+7|8)?\s*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s-]*(\(?(доб.)\s(\d+)\)?)?)?,([^,]*@\w*.\w*)?"
pattern_empty_phone = r"\+7\(\)--\s"
result = []
data_dict = {}
for i in contacts_list:
    text = ','.join(i)
    res = re.sub(pattern, r'\1,\2,\3,\4,\5,+7(\8)\9-\10-\11 \13\14,\15', text)
    res = re.sub(pattern_empty_phone, '', res)
    r = res.split(',')
    key = ','.join(r[:2])
    value = r[2:7]
    if key in data_dict:
        for d, item in enumerate(value):
            if item == '':
                value[d] = data_dict.get(key)[d]
    data_dict[key] = value

for k, v in data_dict.items():
    data_string = k.split(',') + v
    result.append(data_string)


with open("data/phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(result)
