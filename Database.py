import json

class DB:

    def register_user(self,username,email,password):
        with open("db.json","r") as f:
            users=json.load(f)

            if email in users:
                return 0
            else:
                users[email]=[username,password]

                with open("db.json","w") as wf:
                    json.dump(users,wf)
                return 1



    def check_login(self,email,password):
        with open("db.json","r") as f:
            users=json.load(f)

        if email in users:
            if password ==users[email][1]:
                return 1
            else:
                return 0
        else:
            return -1