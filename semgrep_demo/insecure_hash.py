import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # 🚨 Insecure hashing algorithm

def store_password(password):
    hashed = hash_password(password)
    print(f"Storing password hash: {hashed}")
    return hashed

def verify_password(input_password, stored_hash):
    return hash_password(input_password) == stored_hash

def main():
    original = "secretpass"
    hash_val = store_password(original)
    print("Verifying password...")
    if verify_password("secretpass", hash_val):
        print("Password verified!")
    else:
        print("Password mismatch!")

if __name__ == "__main__":
    main()
