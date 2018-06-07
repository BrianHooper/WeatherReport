from datetime import datetime
import pickle
import sys

filename = "events.bin"


class Event:
    def update_time(self, date, time):
        """Returns a date object with the hour and minute updated

        :param date: date to modify
        :param time: time as string formatted %H:%M
        :return: formatted date object
        """
        udate = datetime.strptime(time, "%H:%M")
        return date.replace(hour=udate.hour, minute=udate.minute)

    def to_date(self, year, month, day):
        """Converts string year, month, day to date object

        :param year: year string
        :param month: month string (full name i.e. January, February
        :param day: day string
        :return: formatted date object
        """
        return datetime.strptime(year + " " + month + " " + day, "%Y %B %d")

    def __init__(self):
        """constructor"""
        now = datetime.now()
        self.desc = input("Description: ")
        # print("Year: ")
        year = input("Year: ")
        if len(year) == 0:
            year = str(now.year)
        month = input("Month: ")
        if len(month) == 0:
            month = str(now.strftime("%B"))
        day = input("Day: ")
        if len(day) == 0:
            day = str(now.day)
        self.date = self.to_date(year, month, day)
        time = input("Time: ")
        if len(time) > 0:
            self.date = self.update_time(self.date, time)

    def __str__(self):
        """overrides str() method
        :return: string representation
        """
        output = str(self.date.strftime("%Y-%m-%d"))
        output += "\t" + self.desc
        if int(self.date.hour) != 0 or int(self.date.minute) != 0:
            output += "\t" + str(self.date.strftime("%I:%M %p"))
        return output


def print_events(events):
    """Outputs each event to the console
    :param events: list of event objects
    :return: None
    """
    if len(events) == 0:
    	print("There are no events.")
    else:
    	for x in range(0, len(events)):
        	print("[" + str(x) + "] " + str(events[x]))


def save_events(events):
    """Sorts, Pickles and saves events to a binary file
    :param events: list of events
    :return: None
    """
    events.sort(key=lambda x: x.date)
    binary_file = open(filename, mode='wb')
    pickle.dump(events, binary_file)
    binary_file.close()


def read_events():
    """Reads pickled events from a binary file
    :return: list of event objects
    """
    binary_file = open(filename, mode='rb')
    events = pickle.load(binary_file)
    binary_file.close()
    return events


def add_event():
    """Creates a new event and saves it
    :return: None
    """
    events = read_events()
    events.append(Event())
    save_events(events)


def delete_event():
    """Removes an event by index
    :return: None
    """
    events = read_events()
    print_events(events)
    index = -1
    user_input = input("Index: ")
    try:
        index = int(user_input)
    except ValueError:
        exit(1)
    if index < 0 or index >= len(events):
        return
    else:
        del events[index]
        save_events(events)


def clean_events():
    """Automatically removes events from the past
    :return: None
    """
    events = read_events()
    now = datetime.now()
    to_delete = []
    for x in range(0, len(events)):
        if events[x].date < now:
            to_delete.append(x)
    for x in range(0, len(to_delete)):
        del events[x]
    save_events(events)


# Run the program based on parameters
clean_events()
if len(sys.argv) > 1:
    if sys.argv[1] == "add":
        add_event()
    elif sys.argv[1] == "rm":
        delete_event()
    else:
        print("Useage: ")
        print("\t" + sys.argv[0])
        print("\t" + sys.argv[0] + " add")
        print("\t" + sys.argv[0] + " rm")
else:
    print_events(read_events())
