import psycopg2
from app.models.user import User


class DataBase:
    def __init__(self):
        # self.conn = psycopg2.connect(dbname='iya_service_docker', user='ipa', 
        #                 password='password', host='localhost')
        self.conn = psycopg2.connect(dbname='iya_service_docker', user='postgres', host='localhost')

        print(self.conn.info)


    def register_user(self, user) -> None:
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("insert into users (nickname, password, email)"
                "values (%s, %s, %s)", (user.username, user.password, user.email))


    def login_user(self, user) -> tuple: 
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("select user_id, nickname, email, password from users "
                "where nickname = %s and password = %s", (user.username, user.password))

                res = cur.fetchone()
                print(res)
                
                if res != None and res[1] == user.username and res[3] == user.password:
                    return (True, res[0])

                return (False)

    def find_user(self, user) -> bool:
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("select 1 from users "
                "where nickname = %s", (user.username))

                res = cur.fetchone()
                return res


    def check_session(self, session: str) -> bool:
         with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("select 1 from sessions "
                "where session_hash = %s", (session))

                res = cur.fetchone()
                if res != None:
                    return True

                return False


    def create_session(self, user_id, session) -> None:
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("insert into sessions (session_hash, user_id)"
                "values (%s, %s )", (session, user_id))
        pass

    def logout_user(self, user):
        pass



db = DataBase()