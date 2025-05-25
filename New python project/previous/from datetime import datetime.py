from datetime import datetime

def greet(name):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello, {name}! The current time is {current_time}.")

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greet(user_name)