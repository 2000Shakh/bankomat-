from bson import ObjectId
from pymongo import MongoClient

from pymongo.results import UpdateResult


class User:

    def __init__(self, name=None, surname=None, card=None, pin_kod=None, balance=None):
        self.name = name
        self.surname = surname
        self.card = card
        self.pin_kod = pin_kod
        self.balance = balance

    def to_dict(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'card': self.card,
            'pin_kod': self.pin_kod,
            'balance': self.balance
        }


class Database:

    def __init__(self):
        cluster = MongoClient('mongodb+srv://Shakhzod:19912000@cluster0.rj0wh.mongodb.net/Bank?retryWrites=true')
        self.db = cluster["Bank"]
        self.collection = self.db["Users"]

    def insert_one_user(self, user):
        return self.collection.insert_one(user)

    def insert_many_user1(self, users):
        for user in users:
            self.insert_one_user(user.name, user.surname, user.card, user.pin_kod, user.balance)

    def insert_many_user(self, users: list):
        return self.collection.insert_many(users)

    def get_all_user(self):
        return  self.collection.find()

    def get_one_user(self):
        return self.collection.find_one()

    def get_one_user_by_name(self, name):
        return self.collection.find({'name': name})

    def get_one_by_card(self, card):
        return self.collection.find({"card": card})

    def get_one_user_by_surname(self, surname):
        return self.collection.find({'name': surname})

    def update_by_pin_kod(self, pin_kod, balance):
        a = {"pin_kod": pin_kod}
        b = {"$set": {"balance": balance}}
        self.collection.update_one(a, b)

    def update_by_id(self, _id, balance):
        a = {"_id": ObjectId(_id)}
        b = {"$set": {"balance": balance}}
        self.collection.update_one(a, b)








    # def delet_by_balance(self,balance):
    #     balance =({"balance":balance}{"name"})




# delete
# one
# many
# update
# myquery = { "address": {"$regex": "^S"} }
#
# x = mycol.delete_many(myquery)


if __name__ == "__main__":
    user1 = User('Anvar', 'Bekzodov', '1234 5678 6789 3456', '1111', 0)
    user2 = User("Ulug'bek", 'Bekzodov', '4444 5678 6789 3456', '2222', 1000)
    db = Database()

    # # # bitta foydalanuvchini kiritish
    # result = db.insert_one_user(user1.to_dict())
    # print('insert_one_user', result.inserted_id)
    #
    # # birdan ko'p foydalanuvchini kiritish
    # result = db.insert_many_user(users=[user1.to_dict(), user2.to_dict()])
    # print('insert_many_user', result.inserted_ids)
    #
    # # hammasini olish
    # for user in db.get_all_user():
    #     print(user)

    # bittasini olish


    db.update_by_pin_kod(5555, 1000)

    db.update_by_id("60ebf53dfda259a3a42c95c4", 2000)




    # for user in db.get_one_by_card("1234 5678 6789 3456"):
    #     print(user)
