import json
from selector import DatabaseSelector


class User:
    '''Represents a user in the system with methods for user registration, login, 
    show all existing users, sending message, check inbox and chech only unread messages.'''


    def __init__(self):
        self.active_user = ''
        self.db = DatabaseSelector().connection_db_manager()


    def register(self, username, password, is_admin='false'):
        '''Adding a new user'''

        msg = self.db.add_user(username, password, is_admin)
        return json.dumps(msg, indent=1)


    def login(self, username, password):
        '''Login user function'''

        msg, self.active_user = self.db.login_user(username, password)
        return json.dumps(msg, indent=1)


    def users_list(self):
        '''return list of existing users'''

        if self.active_user != '':
            all_users = self.db.get_users()
            return json.dumps(all_users)

        else:
            return json.dumps("You have to be logged to check list of users", indent=1)


    def send_message(self, username, message):
        '''sending message to other users'''

        if not self.active_user:
            return json.dumps('Command available only for logged users', indent=1)

        if self.active_user == username:
            return json.dumps("You can't send message to yourself", indent=1)

        if self.db.count_unread(username) >= 5 and not (self.db.is_user_admin(self.active_user) or self.db.is_user_admin(username)):
            msg = f'Message could not be sent, mailbox user {username} is full'
        else:
            msg = self.db.send_message(username, message, self.active_user)

        return json.dumps(msg, indent=1)


    def check_inbox(self, query):
        '''return messages in user inbox'''

        if self.active_user != '':
            if len(query)>1 and self.db.is_user_admin(self.active_user) is True:
                msg = self.db.get_message(query[1])

            elif len(query)>1 and self.db.is_user_admin(self.active_user) is False:
                msg = 'You do not have permission to check another user mail'

            else:
                msg = self.db.get_message(self.active_user)
                self.db.change_from_unread(self.active_user)

        else: msg = 'First you must log in!'
        return json.dumps(msg, indent=1)


    def check_unread_messages(self):
        '''return only unread messages in user inbox'''

        if self.active_user != '':
            if self.db.is_msg_unread(self.active_user):
                msg = self.db.get_unread_message(self.active_user)
                self.db.change_from_unread(self.active_user)
            else:
                msg = "Your unread message inbox is empty"
        else:
            msg = 'First you must log in!'
        return json.dumps(msg, indent=1)
