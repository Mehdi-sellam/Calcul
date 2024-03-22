# THIS PROGRAM CALCULATES THE USERS AGE IN SECONDS;
from datetime import datetime
from multiprocessing.resource_sharer import stop

#This function detects the leap years between two periods "current date , date of birth";
def leapdays(y1, y2):

    y1 -= 1

    y2 -= 1

    return (y2//4 - y1//4) - (y2//100 - y1//100) + (y2//400 - y1//400)


#This function calculates the number of leap years between "current year , year of birth";
#After that it calculates the simple years without the leap years;
def different_years(current_date, birth_date): 
    leap_years = leapdays(birth_date.year, current_date.year)
    simple_years = current_date.year - birth_date.year - leap_years
    return {"leap_years" : leap_years, "simple_years" : simple_years, "total_years" : leap_years + simple_years}


#This function returns the number of months that the user lived after his birthday passed;
def different_months(current_date, birth_date):
    return birth_date.month - current_date.month

    
#This function returns the number of days that the user lived after the months are calculated;
def different_days(current_date, birth_date):
    return birth_date.day - current_date.day


#This function bellow uses the above functions to return the value of the user's age in seconds;
def age_in_seconds(leap_years, simple_years, different_month, different_days):
    age_in_days = leap_years * 366 + simple_years * 365

    if different_month < 0 :
        age_in_months = (leap_years+simple_years) * 12 + abs(different_month) # abs return the value to posivite number even if it is a negative value;
        # this means that the user have lived the diffrent months calculated;

        if different_days <0:
            age_in_days = (age_in_months * 30) + different_days
            # this means that the user have lived the diffrent days calculated so it will be added to be calculated later on in seconds;

        else:
            age_in_days = (age_in_months * 30) - different_days
            # this means that the user havn't lived the diffrent days calculated so it wont be added to be calculated later on in seconds;

    else:
        age_in_months = (leap_years+simple_years) * 12 - abs(different_month)
        # this means that the user havn't lived the diffrent months calculated;
        
        if different_days <0:
            age_in_days = (age_in_months * 30) + different_days
            # this means that the user have lived the diffrent days calculated so it will be added to be calculated later on in seconds;

        else:
            age_in_days = (age_in_months * 30) - different_days
            # this means that the user havn't lived the diffrent days calculated so it wont be added to be calculated later on in seconds;
            
    return age_in_days * 24 * 3600


# This function returns a false value if the entred information doesn't much the date formate;
def validate(date_text):
        try:
            datetime.strptime(date_text, '%d/%m/%Y')
            return True
        except :
            return False

stop_prgrm = False
while stop_prgrm == False:
    given_date = str(input('Enter year of birth dd/mm/yy: '))
    if validate(given_date) == True:
        birth_date = datetime.strptime(given_date, '%d/%m/%Y')

        # Here where the secondary fuctions are being called.
        month = different_months(datetime.now(), birth_date)
        days = different_days(datetime.now(), birth_date)
        leap_years = different_years(datetime.now(), birth_date)["leap_years"]
        simple_years = different_years(datetime.now(), birth_date)["simple_years"]

        # Here where the main fuunction "age_in_seconds" will be called inculuding all the neccesary arguments;
        print("You have been alive for : " , age_in_seconds(leap_years=leap_years, simple_years=simple_years, different_month=month, different_days=days) , " Seconds ! 🙂")
        answer = True
        while answer:
            answer = str(input('If You want to stop the programm type "stop" else type "continue" :'))
            if answer == "stop":
                print("Programme Ends Thank You ")
                stop_prgrm = True
                break
            elif answer == "continue":
                break
            else:
                pass
    
# this is the END of this program;