# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:56:21 2024

@author: PASAM
"""

def simple_interest(principal, rate, time):
    """
    Calculate simple interest
    :param principal: principal amount
    :param rate: interest rate (percentage)
    :param time: time duration (in years)
    :return: simple interest
    """
    return (principal * rate * time) / 100

# Example usage:
principal_amount = float(input("Enter principal amount: "))
interest_rate = float(input("Enter interest rate (in percentage): "))
time_period = float(input("Enter time period (in years): "))

simple_interest_amount = simple_interest(principal_amount, interest_rate, time_period)
print("Simple Interest:", simple_interest_amount)