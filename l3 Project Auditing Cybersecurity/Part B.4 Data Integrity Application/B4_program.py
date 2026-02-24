import hashlib

def calculate_md5(file_path):
    """
    Calculate MD5 hash of a file
    """
    hash_md5 = hashlib.md5()
    
    try:
        with open(file_path, "rb") as file:
            # Read the file in chunks to handle large files efficiently
            for chunk in iter(lambda: file.read(4096), b""):
                hash_md5.update(chunk)
        
        # Get the hexadecimal digest of the hash
        # TODO: Return the MD5 hash as a hexadecimal string
        return hash_md5.hexdigest()  # ← This is the ONE LINE you need to write
    
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    except Exception as e:
        return f"Error: {e}"

def main():
    """
    Main function to calculate and display MD5 hash
    """
    file_name = "data.txt"
    print(f"Calculating MD5 hash for '{file_name}'...")
    
    hash_value = calculate_md5(file_name)
    
    print(f"\nMD5 Hash: {hash_value}")
    
    # Optional: Verify with command line output
    print("\n" + "=" * 50)
    print("VERIFICATION:")
    print("You can verify this hash using terminal command:")
    print(f"md5sum {file_name}")
    print("=" * 50)

if __name__ == "__main__":
    main()