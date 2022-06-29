import datetime
def date_time(K):
    pass

if __name__=="__main__":
    print("""
    1.Display current date in dd-mm-yyyy format
    2.Display current date in the following format of : Monday, April 18,2022
    3.Display current date in the format of MM/DD/YY
    4.Display current time in HH:MM:SS
    5.Display whether current time is AM or PM
    """)
    K=int(input("Enter your choice"))
    print(date_time(K))
