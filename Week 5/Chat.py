#Mario Padilla-Chee 149813 Intro to Programming Final Project 
import re
class ChatSessions:
    def __init__(self,filename):
        self.numLines = 0
        self.TagsList = []
        self.MembersList = []
        self.TimesList = []
        self.UniqueMembersList = []
        self.UniqueTagsList = []
        self.MessageList = []
        self.UserSysList=[]
        self.filename=filename
        
        
    def GetNumLines(self):              #function to count lines in file
        f = open(self.filename, "r")
        records = f.readlines()
        for record in records:
            self.numLines+=1            #Counter is updated to +1 through each loop iteration
        return self.numLines

    def GetTagsList(self):              #Function to get all Tags(repeated) from file
        f = open(self.filename, "r")
        records = f.readlines()
        for record in records:
            x=re.findall("^T.?\d",record) 
            self.TagsList.extend(x)
        return self.TagsList
        

    def GetUniqueTagsList(self):        #Function to output unique tag (no-repeat)
        self.GetTagsList()              #Run GetTags function
        self.uniquetagsset=set(self.TagsList) #Convert output of function to set to eliminate repeats
        self.UniqueTagsList=list(self.uniquetagsset) #convert set to list to sort and display
        self.UniqueTagsList.sort()                  #sort list
        return(self.UniqueTagsList)
    
    def GetTimesList(self):             #Function to ouput timestamps
        f = open(self.filename, "r")
        records = f.readlines()
        for record in records:
            x=re.search("(\s+?\d+\s)",record)
            self.TimesList.append(record[x.start()+1:x.end()-1])
        return(self.TimesList)
    
    def GetMembersList(self):           #function to output all member instances (repeated)
        f = open(self.filename, "r")
        records = f.readlines()
        for record in records:
            x=re.search("(\s[A-Za-z]*\s)",record)
            self.MembersList.append(record[x.start()+1:x.end()-1])
        return(self.MembersList)
    
    def GetUniqueMembersList(self):     #function to output unique member (no-repeat) instances
        self.GetMembersList()           #call GetMember function
        self.uniquemembersset=set(self.MembersList) #Turn function output to set to eliminate repeats
        self.UniqueMembersList=list(self.uniquemembersset)  #turn set to list to output
        return(self.UniqueMembersList)
    
    def GetUserSysList(self):           #function to retrieve UserSystem symbol
        f = open(self.filename, "r")    
        records = f.readlines()
        for record in records:
            x=re.search("\s(\D)\s",record)
            self.UserSysList.append(record[x.start()+1:x.end()-1])
        return(self.UserSysList)
    
    def GetMessageList(self):           #function to retrieve messages from file
        f = open(self.filename, "r")
        records = f.readlines()
        for record in records:
            x=re.search("\s\D\s(.*)",record)
            self.MessageList.append(record[x.start()+2:x.end()].strip())
        return(self.MessageList)
    
#Instantiate class    
myObj=ChatSessions("iphone_07_18-1.annot") #Insert filename

#Instantiate each function to produce output
num=myObj.GetNumLines()
tag=myObj.GetTagsList()
uniquetags=myObj.GetUniqueTagsList()
time=myObj.GetTimesList()
members=myObj.GetMembersList()
uniquemembers=myObj.GetUniqueMembersList()
usersys=myObj.GetUserSysList()
messages=myObj.GetMessageList()

#print desired output
print(num)
