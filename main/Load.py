from datetime import datetime
from itertools import takewhile, dropwhile
class Load():

    def isDate(line, date):
        if(line.startswith('*')):
            year, day, month, hour, min, sec = line.split()[1:]
            rowDate = datetime(int(year), int(month), int(day), int(hour), int(min), int(sec.split(".")[0]))

            return rowDate != date
        else:
            return True

    def isRow(line):
        return not line.startswith('*')

    def load_data(file, date, pos):

        file = open("/home/christian/PycharmProjects/pythonProject/data/odts_prd20200206_0130.sp3")

        # Drops all lines until search date
        skip=dropwhile(lambda line: Load.isDate(line, date), file)
        # Drops date header line
        next(skip)
        # Takes date rows
        lines=takewhile(Load.isRow,skip)


        for line in lines:
            line_split = line.split()
            if pos == line_split[0]:
                return line_split[:4]

        return None

