import math

small_pizza_r=0.30
big_pizza_r=0.40
family_pizza_r=0.50
small_pizza_price=29.0
big_pizza_price=36.5
family_pizza_price=44.5

small_area = math.pi*(pow(small_pizza_r,2))
big_area = math.pi*(pow(big_pizza_r,2))
family_area =math.pi*(pow(family_pizza_r,2))

print('Small pizza, price for 1m^2 \t %.2f' % (small_pizza_price/small_area), 'zł')
print('Big pizza price for 1m^2    \t %.2f' % (big_pizza_price/big_area), 'zł')
print('Family pizza price for 1m^2 \t %.2f' % (family_pizza_price/family_area), 'zł')