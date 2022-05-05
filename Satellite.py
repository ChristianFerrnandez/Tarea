import re


class Satellite:

    def searchbyname(self):

        file = open('data/odts_prd20200206_0130.sp3', "r")

        name = input("Enter the name: ")

        lines = file.readlines()

        mylist = []
        idx = 0

        for line in lines:

            if name in line:
                mylist.insert(idx, line)
                idx += 1
                file.close()

            if len(mylist) == 0:
                print("\n\"" + name + "\" is not found")
            else:
                lineLen = len(mylist)
            for i in range(lineLen):
                print(end=mylist[i])
            print()

    def searchbydate(self):
        file = open('data/odts_prd20200206_0130.sp3', "r")

    def options(self):
        answer = input("Do you want to search by date or name: ")
        if answer == "name":
            self.searchbyname()

    satellite = Satellite()

    satellite.searchByName()
