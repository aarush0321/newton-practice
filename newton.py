def dx(epsilon, x, function):
    return (function(x+epsilon)-function(x-epsilon))/(2*epsilon)

def dx2(epsilon, x, function):
    return (function(x+epsilon) - 2*function(x) + function(x-epsilon))/(epsilon**2)
    
def newton_optimization(x0, function, epsilon = 0.005):
    tolerance = 0.5
    update = 100
    while update >= tolerance:
        first_derivative = dx(epsilon, x0, function)
        second_derivative = dx2(epsilon, x0, function)
        next_x = x0 - first_derivative/second_derivative
        update = next_x - x0
        x0 = next_x
        
    return x0
