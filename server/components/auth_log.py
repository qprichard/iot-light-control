from components.db import my_database as db

class AuthLog():
    def get(self, uid=None, limit=None):
        try:
            if uid == None:
                results = db.select('auth_log', limit=limit, order="desc");
            else:
                results = db.select('auth_log', conditions=[('card_uid', uid)], limit=limit, order="desc")

            response = {}
            count = 0
            for result in results:
                response[count] = result
                count += 1
            return response
        except Exception as e:
            print(e)
            return 1

    def delete(self, conditions=None):
        try:
            if conditions == None:
                db.delete('auth_log')
            else:
                db.delete('auth_log', conditions=conditions)

            return self.get()
        except Exception as e:
            return 1
