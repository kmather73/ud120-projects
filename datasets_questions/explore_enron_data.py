#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pandas
import math
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

count_POI = 0
df = pandas.DataFrame(enron_data)
print df
#for person in enron_data:
#    if enron_data[person]['poi'] == 1:
#        count_POI += 1
#print count_POI

#
#for item in enron_data['PRENTICE JAMES']:
#    print item +"\n"

print 'James total stock values is $' + str(enron_data['PRENTICE JAMES']['total_stock_value'])

print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

#for person in enron_data:
#    if person.startswith('L'):
#        print person

print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print enron_data['SKILLING JEFFREY K']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']
print enron_data['LAY KENNETH L']['total_payments']

nan_sal =  enron_data['YEAP SOON']['email_address']
nan_email = enron_data['GRAMM WENDY L']['salary']

email_count = 0
for person in enron_data:
    print person + " " + str(enron_data[person]['salary'])  +'\n'
    if enron_data[person]['email_address'] != nan_email:
        email_count += 1
print email_count


salary_count = 0
for person in enron_data:
    if enron_data[person]['salary'] != nan_sal:
        salary_count += 1
print salary_count
