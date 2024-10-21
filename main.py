def func() -> str:
    
    """Print a message indicating that the function was called."""
    print ("I´m inside the function")
    

def my_name_is(name: str) -> str:
    """
    Print a message with the provided name in the argument.
    
    Args:
        name (str): Gets printed.
    """
    print("My name is {name}")
    
    
def sum_six(num: int) -> int:
   """
   Add the give nnumber to the number six.
   
   Args:
       num (int): The number that's added to the number six.
   
   Returns:
       int: The sum of six plus the given number.
    """
   return 6 + num


def sum_numbers(a: int, b: int) -> int:
    """
    Sum the numbers given.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def usd_to_eur(a: int) -> float:
    """
    Convert USD to EUR.
    
    Args:
        a (int): The amount in USD to be converted into EUR.
    
    Returns:
        float: The amount converted to EUR at a rate of 0.8.
    """
    return a * 0.8