# append_file.py

def append_file(source_file, target_file):
    """Append all lines from source_file to the end of target_file."""
    with open(source_file, 'r', encoding='utf-8') as src:
        data = src.read()
    
    with open(target_file, 'a', encoding='utf-8') as dst:
        dst.write(data)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python append_file.py <source_file> <target_file>")
        sys.exit(1)

    source = sys.argv[1]
    target = sys.argv[2]
    append_file(source, target)
    print(f"Appended contents of {source} to {target}")
