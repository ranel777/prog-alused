import math


def print_hello() -> str:
    print("Hello")
    
    
def get_hello() -> str:
    return "Hello"


def ask_name_and_greet_user() -> str:
    """
    Ask for user´s name and greet them.
    
    If the name is 'Thanos', it sends a special message. Otherwise, greets the user.
    """

ClientInput = input("Please enter you name: ")
FinalName = ClientInput.capitalize()

if FinalName == "Thanos":
    print("Get out of here, Thanos! Nobody wants to play with you!")
else:
    print(f"Hi, {FinalName}. Would you like to have a hamburger?")
    
    
def calculate_hypotenuse_length(a: float, b: float) -> float:
    return math.hypot(a, b)

def calculate_cathetus_length(a: float, c: float) -> float:
    return math.sqrt


if __name__ == '__main__':
    print_hello() #should be printing "Hello"
    hello = get_hello() #should return "Hello"
    print(hello) #checks the value of  hello variable
    ask_name_and_greet_user() #should be asking for the users name and greet them
    print(calculate_hyptenuse_length(3, 4)) #should print 5.0
    print(calculate_cathetus_length(3, 5)) #should print 4.0
    