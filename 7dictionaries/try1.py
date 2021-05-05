dictionary = {
"name": "berlina",
"old": "eighteen",
"address": "indonesia",
"year": 2001
}

a = dictionary["address"]

#the syntax below is changed value
dictionary["year"] = 2002

if "year" in dictionary:
    print ('yes, \'year\' is available you can check it')
print (dictionary)
print (a)


