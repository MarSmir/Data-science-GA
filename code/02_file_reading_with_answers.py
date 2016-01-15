'''
Lesson on file reading using Airline Safety Data
https://github.com/fivethirtyeight/data/tree/master/airline-safety
'''

airlines = """Aer Lingus,Aeroflot*,Aerolineas Argentinas,Aeromexico*,Air Canada,Air France,
Air India*,Air New Zealand*,Alaska Airlines*,Alitalia,All Nippon Airways,American*,
Austrian Airlines,Avianca,British Airways*,Cathay Pacific*,China Airlines,Condor,
COPA,Delta / Northwest*,Egyptair,El Al,Ethiopian Airlines,Finnair,Garuda Indonesia,
Gulf Air,Hawaiian Airlines,Iberia,Japan Airlines,Kenya Airways,KLM*,Korean Air,LAN Airlines,
Lufthansa*,Malaysia Airlines,Pakistan International,Philippine Airlines,Qantas*,
Royal Air Maroc,SAS*,Saudi Arabian,Singapore Airlines,South African,Southwest Airlines,
Sri Lankan / AirLanka,SWISS*,TACA,TAM,TAP - Air Portugal,Thai Airways,Turkish Airlines,
United / Continental*,US Airways / America West*,Vietnam Airlines,Virgin Atlantic,
Xiamen Airlines"""

airlines = airlines.replace('\n','')
# How many airlines are there
airline_count = 1
for letter in airlines:
    if letter == ',':
        airline_count += 1    
    
airlines.count(',') + 1

# How many airlines include the letter 'A' (only capital letters)
count = 0
for letter in airlines:
    if letter == 'A':
        count += 1

# How many airlines include the letter 'A' (include 'A' & 'a')
count = 0
for letter in airlines:
    if letter == 'A' or letter == 'a':
        count += 1

count = 0
for letter in airlines:
    if letter.upper() == 'A':
        count += 1

# create a list of airlines
airline_list = airlines.split(',')

# count every airline that starts with the letter 'A'
count = 0
for airline in airline_list:
    if airline[0] == 'A':
        count += 1
        
# count every airline that includes '*'
count = 0
for airline in airline_list:
    if airline[-1] == '*':
        count += 1


# read the whole file at once, return a single string (including newlines)
# 'rU' mode (read universal) converts different line endings into '\n'
f = open('airlines.csv', 'rU')
data = f.read()
f.close()


# use a context manager to automatically close your file
with open('airlines.csv', 'rU') as f:
    data = f.read()

### EXERCISE
# What is the data type
type(data)
# get the column headers in a list
data[0:124]
end_ind = data.find('fatalities_00_14')
data[0:end_ind]
dir(str)
data[0:end_ind].split(',')



# read the file into a list (each list element is one row)
with open('airlines.csv', 'rU') as f:
    data = []
    for row in f:
        #print row
        data.append(row)

# do the same thing using a list comprehension
with open('airlines.csv', 'rU') as f:
    data = [row for row in f]

# side note: splitting strings
'Hello DAT7 students'.split()
'apple,banana,cherry'.split(',')

# split each string (at the commas) into a list
with open('airlines.csv', 'rU') as f:
    data = [row.split(',') for row in f]

# do the same thing using the csv module
import csv
with open('airlines.csv', 'rU') as f:
    data = [row for row in csv.reader(f)]

# separate the header and data
header = data[0]
data = data[1:]


"""number of available seat kilometers (ASKs), which is defined as the number
   of seats multiplied by the number of kilometers the airline flies"""
   
ask = """320906734,1197672318,385803648,596871813,1865253802,3004002661,869253552,
710174817,965346773,698012498,1841234177,5228357340,358239823,396922563,
3179760952,2582459303,813216487,417982610,550491507,6525658894,557699891,
335448023,488560643,506464950,613356665,301379762,493877795,1173203126,
1574217531,277414794,1874561773,1734522605,1001965891,3426529504,1039171244,
348563137,413007158,1917428984,295705339,682971852,859673901,2376857805,
651502442,3276525770,325582976,792601299,259373346,1509195646,619130754,
1702802250,1946098294,7139291291,2455687887,625084918,1005248585,430462962"""

ask_list = ask.split(',')


for ind, val in enumerate(ask_list):
    print ind, val

# CASTING
# convert kilometers to miles
int(val) * 0.621371

# ZIP 
zip(airline_list, ask_list)

# TUPLE UNPACKING
for airline, ask in zip(airline_list, ask_list):
    print airline, ask

'''
EXERCISES:

1. Create a list containing the average number of incidents per year for each airline.
Example for Aer Lingus: (2 + 0)/30 = 0.07
Expected output: [0.07, 2.73, 0.23, ...]
'''

incidents = []
for row in data:
    incident = round((int(row[2]) + int(row[5])) / float(30), 2)
    incidents.append(incident)

# Advanced figure our how to sort by the number of incidents
sorted(zip(airlines_list, incidents), key=lambda x: x[1])


# LIST COMPREHENSIONS
[row for row in data]       # create the original list with no changes
[row[0] for row in data]    # takes the first item from each list in data 
[row for row in data[0]]    # only looks at the first item in data
[row for row in data if len(row) > 1] # list iteration with a conditional
  
# create a list of all airlines that include the word airline
[row[0] for row in data if 'Airlines' in row[0]]

[row[0] if 'Airlines' in row[0] else 'creative name' for row in data]

    
# Part 1
incidents = [round((int(row[2]) + int(row[5])) / float(30), 2) for row in data]

"""
EXERCISES:
2. Create a list of airline names (without the star).
Expected output: ['Aer Lingus', 'Aeroflot', 'Aerolineas Argentinas', ...]

3. Create a list (of the same length) that contains 1 if there's a star and 0 if not.
Expected output: [0, 1, 0, ...]

4. BONUS: Create a dictionary in which the key is the airline name (without the star)
   and the value is the average number of incidents.
Expected output: {'Aer Lingus': 0.07, 'Aeroflot': 2.73, ...}
"""

# Parts 2
airlines = []
for row in data:
    if row[0][-1] == '*':
        airlines.append(row[0][:-1])
    else:
        airlines.append(row[0])


# Parts 2 and 3
airlines = []
starred = []
for row in data:
    if row[0][-1] == '*':
        starred.append(1)
        airlines.append(row[0][:-1])
    else:
        starred.append(0)
        airlines.append(row[0])

# Part 4
airline_incidents = dict(zip(airlines, incidents))


'''
A few extra things that will help you with the homework
'''

# 'set' data structure is useful for gathering unique elements
my_list = [1, 2, 1]
set(my_list)            # returns a set of 1, 2
len(set(my_list))       # count of unique elements

# 'in' statement is useful for lists
1 in my_list            # True
3 in my_list            # False

# 'in' is useful for strings (checks for substrings)
my_string = 'hello there'
'the' in my_string      # True
'then' in my_string     # False

# 'in' is useful for dictionaries (checks keys but not values)
my_dict = {'name':'Alex', 'title':'Hey You!'}
'name' in my_dict       # True
'Alex' in my_dict      # False

# 'count' method for strings counts how many times a character appears
my_string.count('e')    # 3
