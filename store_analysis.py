# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 11:50:21 2022

@author: ronni
"""

import csv
import math


store_analysis = []

with open("Stores.csv") as stores_csv:
    store_reader = csv.DictReader(stores_csv)
        
    for row in store_reader:
        store_analysis.append(row)
        
print(store_analysis)
        

# Finding the total number of stores
total_stores = 0

for row in store_analysis:
    total_stores += 1

print("The total number of stores is:",total_stores)


# Finding the total and average sales of the store
total_sales = 0

for row in store_analysis:
    sales = int(row["Store_Sales"])
    total_sales += sales
    
print("The total number of sales is: $" + str(total_sales))

average_sales = total_sales / total_stores
average_sales = round(average_sales, 2)

print("The average number of sales for all stores is: $" + str(average_sales))


# The average customers that went to the stores in a day, month, and year
total_customers_in_a_day = 0

for row in store_analysis:
    daily_customers = int(row["Daily_Customer_Count"])
    total_customers_in_a_day += daily_customers
    
print(total_customers_in_a_day, "customers visited the store daily.")
print(round((total_customers_in_a_day / 30), 0), "customers visited the store monthly.")
print(round(((total_customers_in_a_day / 30) / 12), 0), "customers visited the store annually.")

average_customers_in_a_day = round((total_customers_in_a_day / total_stores), 0)
print("Each store averaged", average_customers_in_a_day,"customers in a day.")


# Finding the lowest and highest customer count in a day

customers = []

for row in store_analysis:
    customer = int(row["Daily_Customer_Count"])
    customers.append(customer)

lowest_customer_count = min(customers)
highest_customer_count = max(customers)

print("The lowest customer count recorded in a day was:",lowest_customer_count)
print("The highest customer count recorded in a day was:",highest_customer_count )

# Finding the average size of a store so as to categorize them
total_size_of_stores = 0

for row in store_analysis:
    store_area = int(row["Store_Area"])
    total_size_of_stores += store_area
    
print("The total physical area of all stores is:", total_size_of_stores)

average_size_of_stores = round((total_size_of_stores / total_stores),2)

print("The average area of the stores is:",average_size_of_stores)

bigger_stores = 0
normal_stores = 0
smaller_stores = 0

for row in store_analysis:
    if int(row["Store_Area"]) > average_size_of_stores:
        bigger_stores += 1
    elif int(row["Store_Area"]) == average_size_of_stores:
        normal_stores += 1
    else:
        smaller_stores += 1
        
print("There are", bigger_stores, "big stores in terms of size.")
print("There are", smaller_stores, "small stores in terms of size.")

print("It's clear that smaller stores are the majority of stores in this area.")


# Do bigger stores have more items
items_in_smaller_stores = 0
items_in_bigger_stores = 0

for row in store_analysis:
    if int(row["Store_Area"]) > average_size_of_stores:
        items_in_big_store = int(row["Items_Available"])
        items_in_bigger_stores += items_in_big_store
    else:
        items_in_small_store = int(row["Items_Available"])
        items_in_smaller_stores += items_in_small_store

print("There are",items_in_bigger_stores, "items in bigger stores.")
print("There are",items_in_smaller_stores, "items in smaller stores.")

if items_in_bigger_stores > items_in_smaller_stores:
    print("Bigger stores have more items than smaller stores.")
else:
    print("Smaller stores have more items than bigger stores.")
    
    
