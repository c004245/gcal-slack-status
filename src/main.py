import datetime

def main(calendar, messaging):  
    try :
        start_date = datetime.date.today().strftime("%Y-%m-%d") + 'T00:00:00Z' #utc time
        end_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d") + 'T00:00:00Z'

        events = calendar.get_events(CALENDAR_NAME, start_date, end_date)
        print("events...... "  events)
    except Exception as e:
        print(e)
