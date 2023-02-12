
def get_next_weekday(weekday):
    """Returns the date of the next target weekday. 0=Mon, 1=Tue etc."""
    today = datetime.now().weekday()
    days_diff = (weekday - today) %7        # number of days between today and the target weekday
    return datetime.today().date() + timedelta(days=days_diff)
