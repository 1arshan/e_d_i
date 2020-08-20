# ----Add video material
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

"""
def get_random_alphanumeric_string():
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(6)))
    return result_str
"""


class QuickstartUser(HttpUser):
    wait_time = between(0, 1)
    freq = 0

    def __init__(self, parent):
        super(QuickstartUser, self).__init__(parent)
        self.token = ""
        self.headers = {}

    @task
    def index_page(self):
        self.freq = self.freq + 1
        print(self.freq)

    def on_start(self):
        # self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9" \
        #  ".eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk3ODY3ODk0LCJqdGkiOi" \
        # "JkMjE2OTAxNTYxNDc0NjFjYTE0NGZlNmU2NWZmODQ0NiIsInVzZXJfaWQiOjIwMzV9.mwzswF65fpZCghqWih" \
        # "-gRYprkycfI8F" \
        # "ULjGaeHNYJXo"
        # self.headers = {'Authorization': 'Bearer {}'.format(self.token)}

        subject_link = random.choice(["Physics", "Biology", "Mathematics", "Biology", "Science"])
        standard_link = str(random.randrange(1, 12))
        topic = random.choice(["T1", "T2", "T3", "T4", "T5"])
        video_link = "https://www.youtube.com/watch?v=j1ErIiGqwGg"
        chapter = random.choice(["Ch1", "Ch2", "Ch3", "Ch4", "Ch5"])
        teacher_link = "55"
        self.client.post("/user/testing/", {"subject_link": subject_link, "standard_link": standard_link,
                                            "topic": topic, "video_link": video_link,
                                            "chapter": chapter, "teacher_link": teacher_link})

# "first_name":"arshan",
# "last_name":"agfsdl",
# "phone_number":"94",
# "email":"1arshanahmad@gmail.com",
#  "standard_or_class":"8",
# "password":"palindrome",
# "pincode":"32424"
