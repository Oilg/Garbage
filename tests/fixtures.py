from garbage.api.v1.types import UserModel

# TODO брать коннект и использовать сырые запросы
USER = [
    UserModel(id=1, first_name="Mega", last_name="Azazaev", address="Moscwe", phone="777", email="azazaev@mail.ru", is_active=True), # сделать словарем и передавать **kvarg
]
