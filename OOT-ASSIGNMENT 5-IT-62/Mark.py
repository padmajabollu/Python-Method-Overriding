import operator
from ass5submodule import Student
from operator import itemgetter
from collections import OrderedDict

class Marks(Student):
    
    def __init__(self, prn, name, dob, email, contact, marks):
        Student.__init__(self, prn, name, dob, email, contact)
        self.marks = marks
        
    def __del__(self):
        print("\nDestructor Called")

    def __str__(self):
        return Student.__str__(self)+"\t    "+str(self.marks["OOT"])+"\t     "+str(self.marks["ME"])\
        +"\t      "+str(self.marks["EI"])


    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, marks):
        try:

            if isinstance(marks,dict):
                self.__marks = marks
                
            else:
                raise TypeError("Invalid Object is passed")

        except TypeError:
            print(TypeError)

    

    def display1(self):
        per=((self.marks['OOT']+self.marks['ME']+self.marks['EI'])*100)/300
        if per<=100 and per>=75:
            grade="A"
        elif per<=74 and per>=65:
            grade="B"
        elif per<=64 and per>=55:
            grade="C"
        elif per<=54 and per>=45:
            grade="D"
        elif per<=44 and per>0:
            grade="F"
        else:
            pass
                
        print("\n",self.prn,"\t    ",self.name,"\t",self.dob,"\t",self.email,"\t",self.contact,"\t",self.marks['OOT'],"\t",self.marks['ME'],"\t ",self.marks['EI'],"\t",per,"\t",grade)
        #print("\n",self.prn,"\t     ",self.name,"\t    ",self.dob,"\t     ",self.email,"\t      ",self.contact,"\t  ",self.marks['OOT'],"\t  ",self.marks['ME'],"\t  ",self.marks['EI'])           
        
class MarksData(object):
    slist = {} # DICTIONARY GETS CREATED
    Total=0
    Topper={}
    delete1=0
    
    @staticmethod

    def addStudent():
        prn = input("\nEnter PRN: ")
        #StudentData.roll = StudentData.roll + 1
        name = input("\nEnter the name: ")
        dob = input("\nEnter Date of Birth: ")
        email = input("\nEnter your email id: ")
        contact = input("\nEnter the contact number: ")
        ms = {'OOT':0,'ME':0,'EI':0}   
        for k,v in ms.items():
           while True:
            try:
                    m= int(input("\n{}:".format(k)))
                    if m>0 and m<=100 and m!=None :
                        ms[k]= m  
                        break  
                    else:
                        continue

            except ValueError as e:
                    print("\nEnter Integer Number only .......")   
                    continue       

        """
        for k,v in ms.items():
            print(k, v)
        """    
        MarksData.slist[prn]=Marks(prn,name,dob,email,contact,ms)
        MarksData.Total+=1
         
        
    @staticmethod

    def update():
        while True:
            print("\n1.Update by PRN\n2.exit")
            ch=int(input())
            if ch==1:
                
                p=input("\nEnter PRN to Update the marks : ")
                for k,v in MarksData.slist.items():
                    
                    if k==p:
                        sub=(input("\nEnter subject for Update : "))
                        mar=int(input("\nEnter Marks : "))
                        v.marks[sub]=mar
                        break
                    else:
                        continue
                    print("\nInvalid PRN")


                
            elif ch==2:
                break
            
            else :
                print("\nWrong Choice.......")

            #has_key

    @staticmethod

    def search():
        while True:
            print("\n1.Search by PRN\n2.exit")
            ch=int(input())
            if ch==1:
                
                p=input("\nEnter PRN to Search the marks : ")
                for k,v in MarksData.slist.items():
                    
                    if k==p:
                        print("\n PRN    \t     Name\tDate of Birth\t   Email ID\t      Contact Number \t OOT\t ME\t\t EI")

                        print("\n",k,"\t    ",v.name,"\t",v.dob,"\t",v.email,"\t",v.contact,"\t",v.marks['OOT'],"\t",v.marks['ME'],"\t",v.marks['EI'])
                        break
                    else:
                        continue
                    print("\nInvalid PRN")


                
            elif ch==2:
                break
            
            else :
                print("\nWrong Choice.......")

    
    @staticmethod

    def delete():

        while True:
            print("\n1.Delete by PRN\n2.exit")
            ch=int(input())
            if ch==1:
                
                p=input("\nEnter PRN to Delete the Entry : ")
                for k,v in MarksData.slist.items():
                    
                    if k==p:
                        del MarksData.slist[k]
                        MarksData.delete1+=1
                        MarksData.Total-=1
                        break
                    else:
                        continue
                    print("\nInvalid PRN")


                
            elif ch==2:
                break
            
            else :
                print("\nWrong Choice.......")
        print("\nTotal entries Deleted : {}".format(MarksData.delete1))
    
    @staticmethod

    def noofentries():
        print("\nTotal Entries : {}".format(MarksData.Total)) 
    

    @staticmethod

    def display():


        print("\n PRN    \t     Name\tDate of Birth\t   Email ID\t      Contact Number \t OOT\t ME\t\t EI\tPercentage\tGrade")
        for k,v in MarksData.slist.items():
            v.display1()    
            #print("\n",k,"\t    ",v.name,"\t",v.dob,"\t",v.email,"\t",v.contact,"\t",v.marks['OOT'],"\t",v.marks['ME'],"\t",v.marks['EI'],"\t",b,"\t\t",grade)
                
    @staticmethod

    def topper():
        print("\n PRN    \t     Name\tDate of Birth\t   Email ID\t      Contact Number \t OOT\t ME\t\t EI\tPercentage\tGrade")
        i=0
        for k,v in MarksData.slist.items():
            per=((v.marks['OOT']+v.marks['ME']+v.marks['EI'])*100)/300
            MarksData.Topper[k]=per   
        sorted_x = sorted(MarksData.Topper.items(), key=itemgetter(1),reverse=True)
        for k in sorted_x:
            if i==0:
                
                for a,b in MarksData.Topper.items():
                    if a==k[0]:
                        for p,q in MarksData.slist.items():
                            if p==a :
                                if b<=100 and b>=75:
                                    grade="A"
                                elif b<=74 and b>=65:
                                    grade="B"
                                elif b<=64 and b>=55:
                                    grade="C"
                                elif b<=54 and b>=45:
                                    grade="D"
                                elif b<=44 and b>0:
                                    grade="F"
                                else:
                                    grade=""

                                if (q.marks['OOT']>=40) and (q.marks['ME']>=40) and (q.marks['EI']>=40):
                                    
                    
                                    print("\n",p,"\t    ",q.name,"\t",q.dob,"\t",q.email,"\t",q.contact,"\t",q.marks['OOT'],"\t",q.marks['ME'],"\t",q.marks['EI'],"\t",b,grade) 
                                    i+=1
                                    break
                            else:
                                continue
           

    @staticmethod

    def threetopper():
        i=1
        for k,v in MarksData.slist.items():
            per=((v.marks['OOT']+v.marks['ME']+v.marks['EI'])*100)/300
            MarksData.Topper[k]=per   
        sorted_x = sorted(MarksData.Topper.items(), key=itemgetter(1),reverse=True)
        #print("\n PRN    \t     Name\tDate of Birth\t   Email ID\t      Contact Number \t OOT\t ME\t\t EI\tPercentage")
        print("\n PRN    \t     Name\tDate of Birth\t   Email ID\t      Contact Number \t OOT\t ME\t\t EI\tPercentage\tGrade")

        for k in sorted_x:
            if i!=4:
                
                for a,b in MarksData.Topper.items():
                    if a==k[0]:

                        for p,q in MarksData.slist.items():
                            if p==a :
                                if b<=100 and b>=75:
                                    grade="A"
                                elif b<=74 and b>=65:
                                    grade="B"
                                elif b<=64 and b>=55:
                                    grade="C"
                                elif b<=54 and b>=45:
                                    grade="D"
                                elif b<=44 and b>0:
                                    grade="F"
                                else:
                                    grade=""

                                
                                #for k,v in MarksData.slist.items():
                                if (q.marks['OOT']>=40) and (q.marks['ME']>=40) and (q.marks['EI']>=40):
                                                
                                    print("\n",p,"\t    ",q.name,"\t",q.dob,"\t",q.email,"\t",q.contact,"\t",q.marks['OOT'],"\t",q.marks['ME'],"\t",q.marks['EI'],"\t",b,"\t",grade) 
                                    i+=1
                                    break
                                else:
                                    continue
                

