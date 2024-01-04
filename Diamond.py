def print_diamond(rows):
    for i in range(1, rows + 1, 2):
        print(" " * ((rows - i) // 2) + "*" * i)

    for i in range(rows - 2, 0, -2):
        print(" " * ((rows - i) // 2) + "*" * i)

def main():
    try:
        n = int(input("Masukkan jumlah baris (angka ganjil): "))
        if n % 2 == 0:
            raise ValueError("Masukkan jumlah baris yang ganjil.")
        
        print_diamond(n)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
