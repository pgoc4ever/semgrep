def validate_age(age):
    assert age > 0, "Age must be positive"  
    return age

def get_user_age():
    try:
        age = int(input("Enter your age: "))
        return validate_age(age)
    except Exception as e:
        print("Error:", e)
        return -1

def main():
    age = get_user_age()
    if age > 0:
        print(f"Age accepted: {age}")
    else:
        print("Invalid age.")

if __name__ == "__main__":
    main()
