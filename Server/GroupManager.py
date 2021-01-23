from threading import Thread
from Constants import BUFFERSIZE
from MessageReceiver import messageReceiver
from MessageSender import messageSender


class GroupManager(object):
    def __init__(self):
        self.groups = {}

    def createGroup(self, userName, groupName):
        self.groups[groupName] = [userName]
        print(self.groups)
    
    def joinGroup(self, userName, groupName):
        self.groups[groupName].append(userName)
        print(self.groups)


    def listGroup(self):
        groups_information = {}
        for i in self.groups:
            groups_information[i] = len(self.groups[i])

        return groups_information

groupManager = GroupManager()