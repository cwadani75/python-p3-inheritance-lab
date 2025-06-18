#!/usr/bin/env python

from user import User

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "Functions are reusable blocks of code",
            "Classes help you structure code",
            "Everything in Python is an object"
        ]  # ✅ must be a list with length > 0

    def teach(self):
        return self.knowledge[0]  # You can randomize this if needed
