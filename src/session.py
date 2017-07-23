import time



class Session(object):


    def __init__(self, date, time_start, time_end=None, work=None, breaks=None):
        self.date = date
        self.time_start = time_start
        self.time_end = time_end
        self.work = work
        self.breaks = breaks

    def json(self):

        return {
            'date' : date,
            'time_start' : time_start,
            'time_end' : time_end,
            'work' : work,
            'breaks' : breaks,
        }



    def save_to_file(self):
        ''' saves to current users session file'''
        pass



    def continue_session(self):
        pass
