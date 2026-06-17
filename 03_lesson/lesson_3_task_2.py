from smartphone import Smartphone
catalog = [
    Smartphone("Samsung", "Galaxy S26 Ultra", "+79777421829"),
    Smartphone("POCO", "POCO X8", "+74957556983"),
    Smartphone("Apple", "iPhone 17", "+77846275821"),
    Smartphone("Honor", "Honor Magic 8 Pro 5G", "+79852696969"),
    Smartphone("Realme", "Realme GT 8 Pro", "+78696767564")
]
for smartphone in catalog:
    print(f"{smartphone.brand}, {smartphone.model}, {smartphone.number}")
