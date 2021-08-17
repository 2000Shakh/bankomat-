from database.dbmanager.dbmanager import Database, User

db = Database()
value = int(input(f"Menyudam bittasini tanlang:\n1. Kiritish\n2.Qidirish\n3. O'chirish\n4. O'zgartirish"))
if value == 1:
    user = User()

    user.name = input("Ism")
    user.surname = input("I:")
    user.card = input("I:")
    user.pin_kod = input("I:")
    user.balance = input("I:")

    db.insert_one_user(user.to_dict())
else:
    print("Bunday raqam yo'q")
