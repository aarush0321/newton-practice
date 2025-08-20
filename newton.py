def derivative(epsilon, x, function):
    first_derivative = (function(x+epsilon)-function(x-epsilon))/(2*epsilon)
    second_derivative = (function(x+epsilon) - 2*function(x) + function(x-epsilon))/(epsilon**2)
    return first_derivative, second_derivative

def newton_optimization(x0, function, epsilon = 0.005):
    tolerance = 0.5
    update = 100
    while update >= tolerance:
        first_derivative, second_derivative = derivative(epsilon, x0, function)
        next_x = x0 - first_derivative/second_derivative
        update = next_x - x0
        x0 = next_x
        
    return x0
