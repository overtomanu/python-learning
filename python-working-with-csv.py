# working with CSVs using built-in library

import csv
import os

# execute inside python-learning directory (directory inside which this py file is present)
os.chdir("./Complete-Python-3-Bootcamp-master/15-PDFs-and-Spreadsheets")

# reading CSV file
data = open('example.csv',encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)
print("data_lines[:3] => \n", data_lines[:3])

print("\nprinting first 5 lines of CSV\n")
for line in data_lines[:5]:
    print(line)

print("len(data_lines) => ", len(data_lines))

# collecting emails from first 15 rows, email is the 4th column
all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])
print("all_emails => ", all_emails)

# writing to a new CSV file

# newline controls how universal newlines works (it only applies to text
# mode). It can be None, '', '\n', '\r', and '\r\n'. 
file_to_output = open('to_save_file.csv','w',newline='')

csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'],['4','5','6']])

file_to_output.close()

# writing to existing CSV file
f = open('to_save_file.csv','a',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['new','new','new'])
f.close()

f = open('to_save_file.csv', 'r')
print("\nprinting contents of to_save_file.csv\n")
print(f.read())