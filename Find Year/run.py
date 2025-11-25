
#Brute force method
import re

def main(num):
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    found = False
    for year in range(1000,9334):
        for month in months:
            if find_number(year,month,num) == True:
                found = True
                break
        if found:
            break


def find_number(year,month,num):
    path = f"data/{year}/{month}.txt"
    book = read_book(path)
        
    search_num = re.search(r"\[\[Number of people:\s*(\d+)\]\]", book)
    num_of_people = search_num.group(1)
    if num_of_people:
        if int(num_of_people) == int(num):
            print(f"found the number in {year}")
            return True
    else:
        print("not found")

def read_book(path):
    with open(path) as f:
        return f.read()
    
main(47359253)