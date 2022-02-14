month=int(input("enter month(MM):"))

if(month in[1,3,5,7,8,10,12]):#months with 31 days
    day=int(input("Enter day(DD):"))
    if(1<=day<=31):
        year=int(input("enter year(YYYY):"))
        if(1800<=year<=2025):
            print("input Date(DD/MM/YYYY):",day,"/",month,"/",year)
            if(month==12 and day==31):#last day of the year 
                print("Next Date(DD/MM/YYYY):","1/1/",year+1)#shifting to next year
                
            elif(day==31):#last day of the month
                print("Next Date(DD/MM/YYYY):","1/",month+1,"/",year)#shifting to next month
            else:
                print("Next Date(DD/MM/YYYY):",day+1,"/",month,"/",year)
        else:
            print("invalid year")
    else:
         print("invalid date")
elif(month in[4,6,9,11]):#months with 30 days
    day=int(input("enter day(DD):"))
    if(1<=day<=30):
        year=int(input("Enter year(YYYY):"))
        if(1800<=year<=2025):
            print("input Date(DD/MM/YYYY):",day,"/",month,"/",year)
            if(day==30):#last day of the month
                print("Next Date(DD/MM/YYYY):","1/",month+1,"/",year)#shifting to next month
            else:
                print("Next Date(DD/MM/YYYY):",day+1,"/",month,"/",year)
        else:
            print("invalid year")
    else:
         print("invalid date")
elif(month==2):
    year=int(input("Enter year(YYYY):"))
    if(1800<=year<=2025):
        day=int(input("Enter day(DD):"))
        if(year%4==0):#checking for leap year as they are divisible by 4
            if(1<=day<=29):#for leap year
                print("Input Date(DD/MM/YYYY):",day,"/",month,"/",year)
                if(day==29):#last day of a leap year feb
                    print("Next Date(DD/MM/YYYY):","1/",month+1,"/",year)#shifting to next month
                else:
                    print("Next Date(DD/MM/YYYY):",day+1,"/",month,"/",year)              
            else:
                print("invalid day")
        else:
            if(1<=day<=28):#for non leap year
                print("Input Date(DD/MM/YYYY):",day,"/",month,"/",year)
                if(day==28):#last day of non leap year feb
                    print("Next Date(DD/MM/YYYY):","1/",month+1,"/",year)#shifting to next month
                else:
                    print("Next Date(DD/MM/YYYY):",day+1,"/",month,"/",year)       
            else:
                print("invalid day")     
    else:
        print("invalid year")
else:
    print("invalid month")
