import re
text="Contact us at abc@gmail.com or xyz@yahoo.com"
pattern=r'\w+\@\w+\.\w+'
emails = re.findall(pattern,text)
for email in emails:
    print(email)