def ground_shipping(weight):
  flat_base = 20.00
  if weight <= 2:
    price_per_lb = 2.50
  elif (weight > 2) and (weight <= 6):
    price_per_lb = 3.00
  elif (weight > 6) and (weight <= 10):
    price_per_lb = 4.00
  elif weight > 10:
    price_per_lb = 4.75
  weight_cost = weight * price_per_lb
  return weight_cost + flat_base

def drone_shipping(weight):
  if weight <= 2:
    price_per_lb = 4.50
  elif (weight > 2) and (weight <= 6):
    price_per_lb = 9.00
  elif (weight > 6) and (weight <= 10):
    price_per_lb = 12.00
  elif weight > 10:
    price_per_lb = 14.25
  return weight * price_per_lb

premium_shipping = 125.00

def best_shipping_price(weight):
  drone_price = drone_shipping(weight)
  ground_price = ground_shipping(weight)
  
  if (ground_price < drone_price) and (ground_price < premium_shipping): 
    return The cheapest shipping is ground shipping and the cost is:  + format(ground_price, '.2f')
  elif (drone_price < ground_price) and (drone_price < premium_shipping):
    return The cheapest shipping is drone shipping and the cost is:  + format(drone_price, '.2f')
  elif (premium_shipping < ground_price) and (premium_shipping < drone_price):
    return The cheapest shipping is premium shipping and the cost is:  + format(premium_shipping, '.2f')
  
print(best_shipping_price(4.8))
print(best_shipping_price(41.5))
