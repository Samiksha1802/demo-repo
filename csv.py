import csv
import requests
from bs4 import BeautifulSoup
import lxml
    
r = requests.post('https://opir.fiu.edu/instructor_evals/instr_eval_result.asp', data={'Term': '1175', 'Coll': 'CBADM'})
soup = BeautifulSoup(r.text, "lxml")
    
tables = soup.find_all('table')
print(tables)
    
    
    
print(tables)


writer = csv.writer(open("C:\\Temp\\output_file.csv", 'w'), newline='')

    
for table in tables:
    rows = table.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        if len(cells) == 7:  # this filters out rows with 'Term', 'Instructor Name' etc.
            for cell in cells:
                print(cell.text + "\t", end="") 
                writer.writerow(cell.text)
            print("")  # newline after each row
    print("-------------")  # table delimiter
