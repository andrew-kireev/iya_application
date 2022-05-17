import psycopg2
from app.models.user import User


class DataBase:
    def __init__(self):
        self.conn = psycopg2.connect(dbname='users_service_docker', user='ipa', 
                        password='password', host='localhost')


    def register_user(self, user) -> None:
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("insert into users (username, password, email)"
                "values (%s, %s)", (user.username, user.password, user.email))


    def login_user(self, user) -> User: 
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("select user_id, username, email, password from users "
                "where username = %s and email = %s", (user.username, user.password))

                res = cur.fetchone()
                print(res)


    def logout_user(self, user):
        pass



db = DataBase()