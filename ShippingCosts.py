weight = 1.5
cost = ''

print('Package weight is', weight, 'Pounds')
# Ground Shipping
flat_charge = 20

if weight <= 2:
  cost = weight * 1.50 + flat_charge
elif weight <= 6:
  cost = weight * 3.00 + flat_charge
elif weight <= 10:
  cost = weight * 4.00 + flat_charge
elif weight > 10:
  cost = weight * 4.75 + flat_charge
else:
  print('Error!')

print('Ground Shipping Costs $',cost)

# Premium Shipping
premium_charge = 125
print('Premium Ground Shipping Costs $', premium_charge)

# Drone Shipping 

if weight <= 2:
  cost = weight * 4.50
elif weight <= 6:
  cost = weight * 9.00
elif weight <= 10:
  cost = weight * 12.00
elif weight > 10:
  cost = weight * 14.25
else:
  print('Error!')

print('Drone Shipping Costs $',cost)
