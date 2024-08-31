fruits_cost = [200, 50, 100, 350]

def maxCustom(fruits_cost):
    max_cost = 0
    for cost in fruits_cost:
        if cost > max_cost:
            max_cost = cost
    return max_cost

#Customization function
(print(maxCustom(fruits_cost)))

#Built-in function
print ("The max is ", max(fruits_cost))
print ("The min is ", min(fruits_cost))
