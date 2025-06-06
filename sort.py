"""fruits=['Apple','Jack fruit','Pine apple','Kiwi','Banana','Guava']
fruits.sort(reverse=True)
print(fruits)"""

def  myFunc(e):
    return len(e)

cars=['Jeep','Thar','Ford','Volvo','Duster']
cars.sort(key=myFunc)
print(cars)


"""def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)

print(cars)
"""

def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)
print(cars)