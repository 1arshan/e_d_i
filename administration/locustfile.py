from locust import HttpUser, TaskSet, task
# from locust import ResponseError
import json

"""
class UserBehavior(TaskSet):
    def __init__(self, parent):
        super(UserBehavior, self).__init__(parent)
        self.token = ""
        self.headers = {}

    #@task(1)
    def on_start(self):
        # The on_start method is called
        # when a simulated user starts
        # executing that TaskSet class
        self.token = self.login()
        self.headers = {'Authorization': 'Bearer {}'.format(self.token)}
        self.login()

    #@task
    def login(self):
        # admin login and retrieving it's access token
        response = self.client.post("/token/",
                                    data={'username': 'admin',
                                          'password': 'palindrome'})

        return json.loads(response._content)['access']


class WebsiteUser(HttpUser):
    # The task_set attribute should point
    # to a TaskSet class which defines
    # the behaviour of the user
    task_set = [UserBehavior]
    # tasks = UserBehavior
    min_wait = 0
    max_wait = 1
"""

import random
from locust import HttpUser, task, between
import string



def get_random_alphanumeric_string():
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(6)))
    return result_str


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)
    freq =0
    @task
    def index_page(self):
        self.freq=self.freq+1
        print(self.freq)
    """@task(3)
    def view_item(self):
        item_id = random.randint(1, 10000)
        self.client.get(f"/item?id={item_id}", name="/item")
"""

    def on_start(self):
        first_name = get_random_alphanumeric_string()
        last_name = get_random_alphanumeric_string()
        phone_number = str(random.randrange(10101, 909090))
        email = "1testarshanahmad@gmail.com"
        standard_or_class = str(random.randrange(1, 12))
        password = "palindrome"
        pincode = str(random.randrange(10101, 90909))
        self.client.post("/user/signup/s/", {"first_name": first_name, "last_name": last_name,
                                             "phone_number": phone_number, "email": email,
                                             "standard_or_class": standard_or_class, "password": password,
                                             "pincode": pincode})

# "first_name":"arshan",
# "last_name":"agfsdl",
# "phone_number":"94",
# "email":"1arshanahmad@gmail.com",
#  "standard_or_class":"8",
# "password":"palindrome",
# "pincode":"32424"
