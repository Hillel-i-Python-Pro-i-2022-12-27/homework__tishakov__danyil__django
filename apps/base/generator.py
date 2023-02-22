from faker import Faker

fake = Faker("en_US")


def user_profile():
    login = fake.name()
    email = fake.email()
    password = fake.password()
    return f"{login}, {password}, {email}"


# # def generate_users():
# from faker import Faker
# #     fake = Faker()
# #     for _ in range(50):
# #         user = User.objects.create_user(username=fake.user_name(),password='******',email=fake.email())
# #         user.save()
# #         return user
#
# def create_users():
#     fake = Faker()
#     for rater in Rater.objects.all():
#         if rater.user is None:
#             rater.user = User.objects.create_user(username=fake.user_name()+str(random.randint(1, 999)),
#                                 email= fake.email(),
#                                 password='******')
#             rater.save()
#             print(rater.user.username)
#
# if __name__=="__main__":
#     create_users()
