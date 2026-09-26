#!/usr/bin/env python
# coding: utf-8

# In[62]:


# python d-fee calculator



order_total = input("order total ($): ")
day = input("What day of the week is it?: ")

# validation
Valid_days = {
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
} 
is_valid = True
order_total = 0.0
day_of_week = ""
# setting parameters for the total order amount
try:
     order_total = float(order_total)
     if order_total < 0 or order_total > 10000:
         print("will not calculate order")
         is_valid = False
except ValueError:
        print("Not a valid number.")
        is_valid = False

# Validate day of the week
if day in Valid_days: 
    day_of_week = day
else:
    print(f"not a valid day:")
    is_valid = False

# Calculate the delivery fee using both dependant values
if is_valid:
    if day_of_week == "Friday":
        if order_total > 75.00:
            dfee = 7.50
        else:
            dfee = 3.00
    else:
        if order_total > 75.00:
            dfee = 5.00
        else: 
            dfee = 1.00

# Output

    print(f"{order_total:.2f} on {day_of_week}, delivery fee is {dfee:.2f}.")



# In[ ]:




