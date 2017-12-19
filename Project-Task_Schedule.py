from Tkinter import *
import tkMessageBox

top = Tk()
############ Constant

fileName="taskList.txt"

######################################### 1-Save

def saveTask():        
    f=open(fileName,"a")
    f.seek(0)
    f.write(spinDay.get())
    f.write(",")
    f.write(spinMonth.get())
    f.write(",")
    f.write(spinYear.get())
    f.write(",")
    f.write(w.get())
    f.write("\n")
    w.delete(0 ,len(w.get()))
    f.close()
    tkMessageBox.showinfo("Saved","Task is saved")

#************** GUI save
frame1 = Frame(top)
frame1.pack()


labelSave = LabelFrame(top, text="Save Task")
labelSave.pack(fill="both", expand="yes")

lab1=Label(labelSave,text="Write your Task")
lab1.pack(side=LEFT)
w=Entry(labelSave)
w.pack(side=LEFT)

lab2=Label(labelSave,text="Date(DD.MM.YY)")
lab2.pack(side=LEFT)

spinDay=Spinbox(labelSave,from_=1,to=31,width=2)
spinDay.pack(side=LEFT)

spinMonth=Spinbox(labelSave,from_=1,to=12,width=2)
spinMonth.pack(side=LEFT)

spinYear=Spinbox(labelSave,from_=2017,to=2018,width=4)
spinYear.pack(side=LEFT)

btnSave=Button(labelSave,text="Save",command=saveTask,bg="green")
btnSave.pack(side=LEFT)


######################################### 2-Search 

def searchTask():
    try:
        f=open(fileName,"r").read().split("\n")
        counter=0
        tempList=[]
        for i in f: # make a list to show number of tasks for each specific day ex: 0)task 1 | 1)task2 and so on
            internalList=i.split(",")
            
            if internalList[0] == spinDaySearch.get() and internalList[1]==spinMonthSearch.get() and internalList[2]==spinYearSearch.get():
                tempList.append(internalList[-1])
                

        # If there is a task , listwindows will be created to display. otherwise, messageBox
        if len(tempList) !=0:
            newTop=Toplevel()
            lbl=Label(newTop,text="Task No & Task List")
            lbl.pack()
            btnclose=Button(newTop,text="Close",command=newTop.destroy)
            btnclose.pack()
            scrollbar=Scrollbar(newTop)
            scrollbar.pack(side=RIGHT,fill=BOTH)
            lst=Listbox(newTop,yscrollcommand=scrollbar.set)
            
            for task in tempList: # to show task with given date with task NUMBER 
                value=str(lst.size())+") "+task
                lst.insert(counter,value)
                counter+=1
            scrollbar.config(command=lst.yview)
            lst.pack()
        else:
            tkMessageBox.showinfo("Cool","No task, Relax!")
            
        
    except IOError:# if user press search before creating any task 
        tkMessageBox.showerror("No File","There is no file yet!")

    
#************** GUI search
frame2 = Frame(top)
frame2.pack(pady=10)

labelSearch = LabelFrame(top, text="Search Task")
labelSearch.pack(fill="both", expand="yes")

lab2=Label(labelSearch,text="Pick A Date(DD.MM.YY)")
lab2.pack(side=LEFT)

btnSearch=Button(labelSearch,text="Search",command=searchTask,bg="yellow")
btnSearch.pack(side=LEFT)

spinDaySearch=Spinbox(labelSearch,from_=1,to=31,width=2)
spinDaySearch.pack(side=LEFT)

spinMonthSearch=Spinbox(labelSearch,from_=1,to=12,width=2)
spinMonthSearch.pack(side=LEFT)

spinYearSearch=Spinbox(labelSearch,from_=2017,to=2018,width=4)
spinYearSearch.pack(side=LEFT)


######################################### 3-Update

def updateTask():
    try:
        myfile=open(fileName,"r").readlines()
        tempList=[] #to save only matched task with given date 
        for i in myfile:
            internalList=i.split(",")
            # if search to find a specific task to update    
            if internalList[0] == spinDayUpdate.get() and internalList[1]==spinMonthUpdate.get() and internalList[2]==spinYearUpdate.get():
                tempList.append(i)
                tempList.append('\n')

        # to remove repeated task in original list
        myfile=set(myfile)-set(tempList)
        myfile=list(myfile)
        
        # after finding the exact task, show text entry to update
        showUserTask=(tempList[int(spinUpdateTask.get())].split(',')[-1]).strip()
        updatePanel=Tk()
        updateEntry=Entry(updatePanel)
        updateEntry.pack(side=LEFT)
        updateEntry.insert(0,showUserTask)

        # to save the updated task. its list obj so get value from given in GUI + text
        def saveUpdatedTask():
            tempList[int(spinUpdateTask.get())] = spinDayUpdate.get() + ',' +spinMonthUpdate.get()+','+spinYearUpdate.get()+','+updateEntry.get()
            updatedList=myfile+tempList # combine both lists
            f=open(fileName,"w") # write back tasks
            for row in updatedList:
                f.write(row)
            f.close()            
            tkMessageBox.showinfo("Saved !","Task updated successfully")

            closeUI(updatePanel) # to clsoe the panel windows 
            

        
        updateButton=Button(updatePanel,text="Save",bg="green",command=saveUpdatedTask)
        updateButton.pack(side=LEFT)
        

    except IndexError: # for wrong index
        tkMessageBox.showerror("Can't Find !","There is no task with given details")
    except IOError:# if user press search before creating any task 
        tkMessageBox.showerror("No File","There is no file yet!")    

#************** GUI update
frame3 = Frame(top)
frame3.pack(pady=10)


labelUpdate = LabelFrame(top, text="Update Task")
labelUpdate.pack(fill="both", expand="yes")

lab3=Label(labelUpdate,text="Date(DD.MM.YY) and Task number")
lab3.pack(side=LEFT)


btnUpdate=Button(labelUpdate,text="Update",bg="yellow",command=updateTask)
btnUpdate.pack(side=LEFT)

spinDayUpdate=Spinbox(labelUpdate,from_=1,to=31,width=2)
spinDayUpdate.pack(side=LEFT)

spinMonthUpdate=Spinbox(labelUpdate,from_=1,to=12,width=2)
spinMonthUpdate.pack(side=LEFT)

spinYearUpdate=Spinbox(labelUpdate,from_=2017,to=2018,width=4)
spinYearUpdate.pack(side=LEFT)

spinUpdateTask=Spinbox(labelUpdate,from_=0,to=100, width=3)
spinUpdateTask.pack(side=LEFT)

######################################### 4-Delete
def deleteTask():
    try:
        with open(fileName,"r") as myFileList:
            allContent=myFileList.readlines()
            myFileList.close()

    
        tempList=[]
        for items in allContent:
            item=items.split(',')
            if item[0] == spinDayDelete.get() and item[1]==spinMonthDelete.get() and item[2]==spinYearDelete.get():
                tempList.append(items)

	# to combine both list and have unique values
        allContent=set(allContent)-set(tempList)
        del tempList[int(spinDeleteTask.get())]
        allContent=list(allContent)+tempList
        
        with open(fileName,"w") as newFile:
            for i in allContent:
                newFile.write(i)
                
        tkMessageBox.showinfo("Deleted!","Task is deleted.")    
                    
    except IndexError: # in case of wrong index 
        tkMessageBox.showerror("Can't Find !","There is no task with given details")
    except IOError:# if user press search before creating any task 
        tkMessageBox.showerror("No File","There is no file yet!")
        
#************** GUI delete

frame4 = Frame(top)
frame4.pack(pady=5)

labelDelete=LabelFrame(top,text="Delete Task")
labelDelete.pack(fill="both", expand="yes")

lab4=Label(labelDelete,text="Date(DD.MM.YY) and Task number")
lab4.pack(side=LEFT)

btnDelete=Button(labelDelete,text="Delete",bg="red",command=deleteTask)
btnDelete.pack(side=LEFT)


spinDayDelete=Spinbox(labelDelete,from_=1,to=31,width=2)
spinDayDelete.pack(side=LEFT)

spinMonthDelete=Spinbox(labelDelete,from_=1,to=12,width=2)
spinMonthDelete.pack(side=LEFT)

spinYearDelete=Spinbox(labelDelete,from_=2017,to=2018,width=4)
spinYearDelete.pack(side=LEFT)

spinDeleteTask=Spinbox(labelDelete,from_=0,to=100, width=3)
spinDeleteTask.pack(side=LEFT)

#########################################
def closeUI(self): # to close the update panel
    self.destroy()

    
top.mainloop()
