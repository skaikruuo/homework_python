from address import Address
from mailing import Mailing

address_from = Address("565765", "Йошкар-Ола", "Новая", "5", "13")
address_to = Address("145300", "Подольск", "Кирова", "11", "45")
mailing = Mailing(to_address = address_to, from_address = address_from, track = "45005145009749", cost = 3500)

print(f"Отправление {mailing.track} из "
      f"{mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.flat} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.flat}. "
      f"Стоимость {mailing.cost} рублей.")