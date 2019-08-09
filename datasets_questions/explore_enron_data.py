#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
count_poi = 0
count1 = 0
count2 = 0
largest = 0
import pickle

enron_data = pickle.load(open("/home/jasmeet/PycharmProjects/ML_Udacity/final_project/final_project_dataset.pkl", "rb"))
print(enron_data)

print("")
total_employee = len(enron_data)
print("Total number of employees in dataset: "+str(total_employee))

features_per_person = len(enron_data['METTS MARK'])
print("Number of features available per person: "+str(features_per_person))
print("")

for employee in enron_data:
    if enron_data[employee]['poi'] == 1:
        count_poi = count_poi + 1
    if employee == "PRENTICE JAMES":
        print("Total Stock Value of James Prentice: "+str(enron_data[employee]['total_stock_value']))
        print("")
    if employee == "COLWELL WESLEY":
        print("No. of emails sent by Wesley Colwell to a POI: "+str(enron_data[employee]['from_this_person_to_poi']))
        print("")
    if employee == "SKILLING JEFFREY K":
        print("Stock options exercised by Jeffrey k Skilling: "+str(enron_data[employee]['exercised_stock_options']))
        print("")
    if enron_data[employee]['salary'] != 'NaN':
        count1 = count1 + 1
    if enron_data[employee]['email_address'] != 'NaN':
        count2 = count2 + 1


largest = enron_data['LAY KENNETH L']['total_payments']
highest_earner = "Kenneth Lay"

if enron_data['SKILLING JEFFREY K']['total_payments'] > largest:
    largest = enron_data['SKILLING JEFFREY K']['total_payments']
    highest_earner = "Jeffrey Skilling"

if enron_data['FASTOW ANDREW S']['total_payments'] > largest:
    largest = enron_data['FASTOW ANDREW S']['total_payments']
    highest_earner = "Andrew Fastow"

print("The highest earner is: "+str(highest_earner))
print("With a total earning of: "+str(largest))
print("")

print("No. of Persons of Interests:"+str(count_poi))
print("")
print("People with quantified salary: "+str(count1))
print("People with known email address: "+str(count2))

