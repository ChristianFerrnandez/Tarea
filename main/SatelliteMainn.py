from Load import *
from datetime import datetime

class SatelliteMainn():

    def user_input(file):
        file = open("/home/christian/PycharmProjects/pythonProject/data/odts_prd20200206_0130.sp3")
        date = datetime.strptime(input("Enter the date in this format; YYYY-MM-DD HH:MM:SS "),'%Y-%m-%d %H:%M:%S')
        pos = input("Enter position")
        res = Load.load_data(file,date, pos)


        print(res)
        return None



file = open("/home/christian/PycharmProjects/pythonProject/data/odts_prd20200206_0130.sp3")
sat = SatelliteMainn
sat.user_input(file)
