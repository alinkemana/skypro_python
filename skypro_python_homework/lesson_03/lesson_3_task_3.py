from address import Address

from mailing import Mailing

address_to = Address("101000", "Москва", "Тверская", "12", "45")
address_from = Address("620000", "Екатеринбург", "Ленина", "5", "10")

my_mailing = Mailing(
    to_address=address_to,
    from_address=address_from,
    cost=350,
    track="RU123456789")

print(
    f"Отправление {my_mailing.track} из "
    f"{my_mailing.from_address.code}, "
    f"{my_mailing.from_address.city}, "
    f"{my_mailing.from_address.street}, "
    f"{my_mailing.from_address.house_number} - "
    f"{my_mailing.from_address.apartment_number} в "
    f"{my_mailing.to_address.code}, "
    f"{my_mailing.to_address.city}, "
    f"{my_mailing.to_address.street}, "
    f"{my_mailing.to_address.house_number} - "
    f"{my_mailing.to_address.apartment_number}. "
    f"Стоимость {my_mailing.cost} рублей."
)
