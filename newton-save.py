def dx(epsilon, x, function):
    """
    computes approximation of the first derivative of a specified function at a specific input

    Arguments:
        epsilon: small change in input used to approximate derivative
        x: function input value at which derivative should be calculated
        function: function to calculate derivative of

    Returns:
        dx1: first derivative approximation
    """

    dx1 = (function(x + epsilon) - function(x - epsilon)) / (2 * epsilon)

    return dx1


def dx2(epsilon, x, function):
    """
    comptues approximation of the second derivative of a specified function at a specific input

    Arguments:
        epsilon: small change in input used to approximate derivative
        x: function input value at which derivative should be calculated
        function: function to calculate derivative of

    Returns:
        dx2: second derivative approximation
    """

    dx2 = (function(x + epsilon) - 2 * function(x) + function(x - epsilon)) / (
        epsilon**2
    )

    return dx2


def newton_optimization(x0, function, epsilon=0.005, tolerance=0.5):
    """
    Use Newton's method to find the minimum of a function

    Arguments:
        x0: starting value to iterate from
        function: function being optimized
        epsilon: small change in function inputs used to calculate derivatives

    Returns:
        minima: minimum of function
    """
    x = x0
    update = 100
    while (
        update >= tolerance
    ):  # iterate until update change falls below specific tolerance
        first_derivative = dx(epsilon, x, function)
        second_derivative = dx2(epsilon, x, function)
        next_x = x - first_derivative / second_derivative
        update = next_x - x
        x = next_x

    minima = x

    return minima
