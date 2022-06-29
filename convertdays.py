def convert_days(days):
    pass

if __name__=="__main__":
    days = int(input("Number of days:"))
    result=convert_days(days)
    print("Years |Weeks |Days")
    print('     |'.join(str(x) for x in result))
