import time

def authenticate(user, password):
    if user == "admin" and password == "admin123":  
        return True
    return False

def main():
    print("Authenticating user...")
    if authenticate("admin", "admin123"):
        print("Access granted")
    else:
        print("Access denied")

    time.sleep(1)
    print("End of process.")

if __name__ == "__main__":
    main()
