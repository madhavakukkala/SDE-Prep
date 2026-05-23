## Temperature Conversion

'''

def convert_temperature(temp,unit):
    """ This function converts temperature between Celcius and Farenheit"""

    if unit=="C":
        return temp *9/5 +32 ## Converting Celcius to Fahrenheit
    elif unit== "F":
        return (temp-32)*5/9 ## Fahrenheit to Celcius
    else:
        return None
    

print(convert_temperature(25,"C"))
print(convert_temperature(77,"F"))

'''

## Password Strength Checker


'''

numbers=[1,2,3,4,5,6,7]

lst= list(map( lambda x:x**2, numbers))
print(lst)

## Map multiple Iterables

numbers1=[1,2,3]
numbers2=[4,5,6]

added_numbers=list(map(lambda x,y:x+y , numbers1,numbers2))

print(added_numbers)

'''

list_new=[1,2,3,5,4,57,4,4,34,76,54]

list_naya=list(filter(lambda x:x%2==0, list_new))

print(set(list_naya))


## filter() to check the age is greater than 25 in dictionary



people=[
    {'name': 'Kukkapilla', 'age' : 22},
    {'name': 'Budankay', 'age' : 21},
    {'name': 'Bunny', 'age' : 3},
    {'name': 'Chittipapa', 'age' : 0.5},
]

def age_greater_than_20(person):
    return person['age']>19

print(list(filter(age_greater_than_20, people)))





  

