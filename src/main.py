import datetime
STATUS = {
    "연차": {'status_text': '[연차] Paid Time Off', 'status_emoji': ':desert_island:'},
    "재택": {'status_text': '[재택] Work From Home', 'status_emoji': ':house:'},
}
CALENDAR_NAME = 'c004112@gmail.com'

def main(calendar, messaging):  
    try :
        start_date = datetime.date.today().strftime("%Y-%m-%d") + 'T00:00:00Z' #utc time
        end_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d") + 'T00:00:00Z'

        events = calendar.get_events(CALENDAR_NAME, start_date, end_date)
        print("events...... "  events)

        for event in events:
            user_name, event_name = event["user_name"], event["event_summary"]
            if event_name in STATUS:
                print(user_name, event_name) # ex. 연차 조현욱...
                messaging.update_status(user_name, STATUS[event_name])
    except Exception as e:
        print(e)

if __name__ == '__main__':
    calendar = CalendarClient(calendar_service = GoogleCalendarClient())
    messaging = MessagingClient(messaging_service = SlackClient())
    main(calendar, messaging)