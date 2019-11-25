from components.db import my_database as db

class AuthLog():
    def get(self, uid=None, limit=None):
        try:

            sql = "SELECT auth_log.id, auth_log.card_uid, auth_log.log_date, u.login FROM auth_log";

            sql += " LEFT OUTER JOIN users u on u.card_uid = auth_log.card_uid";

            # if uid is not None:
            #     sql += f" WHERE auth_log.card_uid={uid}";

            sql+=" ORDER BY auth_log.id DESC";

            if limit:
                sql+=f" LIMIT {limit}"
            sql+=";"
            results = db.select(query=sql);
            response = {}
            count = 0

            if not results:
                return {}

            for result in results:
                response[count] = result
                response[count]['granted'] = result['login'] != None
                del response[count]['login']
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
