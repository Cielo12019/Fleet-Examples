import datetime
dt = datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
print(dt)

if __name__ == '__main__':
    from datetime import datetime, timedelta, timezone
    JST = timezone(timedelta(hours=+9))
    dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo=JST)
    print(dt)

# computing time differences 1
if __name__ == '__main__':
    from datetime import datetime, timedelta
    now = datetime.now()
    then = datetime(2016, 5, 23)
    delta = now - then
    print(delta.days)
    print(delta.seconds)

    date_n = datetime.now() - timedelta(days=2)
    print(date_n.strftime('%Y-%m-%d %H:%M:%S'))

# computing time differences 2
if __name__ == '__main__':
    from datetime import datetime, timedelta
    day_delta = timedelta(days=1)
    start_date = datetime.now()
    end_date = start_date + 7*day_delta
    for i in range((end_date - start_date).days):
        print(start_date + i*day_delta)