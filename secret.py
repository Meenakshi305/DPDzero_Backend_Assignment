import secrets

# Generate a random 32-byte (256-bit) secret key
SECRET_KEY = secrets.token_hex(32)

# Print the generated secret key (keep it secret!)
print(SECRET_KEY)