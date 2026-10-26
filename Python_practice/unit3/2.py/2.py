import csv
import json
with open('students.csv','r') as f:
  content=csv.DictReader(f)
  data=list(content)
with open('student.json','w') as f:
  json.dump(data,f)
print("done")