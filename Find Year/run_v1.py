# Implement using binary search
import re

def main(num):
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    year = None
    low = 1000
    high = 9333
    while(low <= high):
        mid = (low + high)//2
        if num < get_number(mid,months[0]):
            high = mid - 1
        elif num > get_number(mid,months[11]):
            low = mid + 1
        else:
            year = mid
            low_month = 0
            high_month = 11
            while low_month <= high_month:
                mid = (low_month + high_month)//2
                value = get_number(year,months[mid])
                if num < value:
                    high_month = mid - 1
                elif num > value:
                    low_month = mid + 1
                else:
                    print(f"found the number in {year}")
                    return
            print("number not found")
            return



def get_number(year,month):
    path = f"data/{year}/{month}.txt"
    book = read_book(path)
        
    search_num = re.search(r"\[\[Number of people:\s*(\d+)\]\]", book)
    num_of_people = search_num.group(1)
    return int(num_of_people)

def read_book(path):
    with open(path) as f:
        return f.read()
    
main(50105034)