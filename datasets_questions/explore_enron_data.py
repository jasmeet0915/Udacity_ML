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
count = 0
import pickle

enron_data = pickle.load(open("/home/jasmeet/PycharmProjects/ML_Udacity/final_project/final_project_dataset.pkl", "rb"))
print(enron_data)

total_employee = len(enron_data)
print(total_employee)
features_per_person = len(enron_data['METTS MARK'])
print(features_per_person)

for employee in enron_data:
    if enron_data[employee]['poi'] == 1:
        count = count + 1
    if employee == "PRENTICE JAMES":
        print("Total Stock Value of James Prentice:")
        print(enron_data[employee]['total_stock_value'])
    if employee == "COLWELL WESLEY":
        print("No. of emails sent by Wesley Colwell to a POI:")
        print(enron_data[employee]['from_this_person_to_poi'])
    if employee == "SKILLING JEFFREY K":
        print("Stock options exercised by Jeffrey k Skilling:")
        print(enron_data[employee]['exercised_stock_options'])


print("No. of Persons of Interests:")
print(count)

