from smartphone import Smartphone

catalog = [
        Smartphone("Samsung", "Galaxy S24", "+79172345678"),
        Smartphone("Apple", "iPhone 15", "+79179876543"),
        Smartphone("Xiaomi", "Redmi Note 13", "+79175032334")]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.number}")
