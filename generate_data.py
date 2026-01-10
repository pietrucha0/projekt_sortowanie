import random

def create_data_file(filename="liczby.txt", count=10000):
    data = [random.randint(0, 100000) for _ in range(count)]
    
    with open(filename, "w") as f:
        for number in data:
            f.write(f"{number}\n")
            
    print(f"Plik {filename} został wygenerowany pomyślnie!")

if __name__ == "__main__":
    create_data_file()