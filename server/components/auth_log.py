from components.db import my_database as db
from datetime import datetime

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

    def get_stats(self, filter='hour'):
        """
        filter = ['hour', 'minute', 'day']
        """
        try:
            sql = "SELECT auth_log.* , u.* FROM auth_log LEFT OUTER JOIN users u on u.card_uid=auth_log.card_uid;"

            results = db.select(query=sql)
            date_count = {}
            for result in results:
                del result['password']
                del result['id']
                result['round_date'] = datetime.strptime(result['log_date'], '%Y-%m-%d %H:%M:%S')
                if filter == 'day':
                    result['round_date'] = result['round_date'].replace(second=0, minute=0, hour=0)
                if filter == 'hour':
                    result['round_date'] = result['round_date'].replace(second=0, minute=0)
                if filter == 'minute':
                    result['round_date'] = result['round_date'].replace(second=0)
                result['round_date'] = result['round_date'].strftime('%Y-%m-%d %H:%M:%S')
                date_count[result['round_date']] = {
                    'granted': 0,
                    'refused': 0
                }

            logs = {}
            for result in results:
                value = 'granted' if result['login'] else 'refused'
                date_count[result['round_date']][value] += 1

                card_uid = result['card_uid']
                round_date = result['round_date']
                if result['login'] is None:
                    continue
                if not round_date in logs:
                    logs[round_date] = {}
                if not card_uid in logs[round_date]:
                    logs[round_date][card_uid] = result
                    logs[round_date][card_uid]['count'] = 1
                else:
                    logs[round_date][card_uid]['count'] += 1

            response = {
                "date_count": date_count,
                "logs": logs
            }
            return response
        except Exception as e:
            print(e)
            return {}
