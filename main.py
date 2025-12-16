import datetime
import os

def main():
    now = datetime.datetime.now()
    user = os.getenv('USER_NAME', 'Unknown User') 

    print("="*40)
    print(f" Python App Started!")
    print(f" Hello, {user}")
    print(f" Current Time: {now}")
    print("="*40)

if __name__ == "__main__":
    main()