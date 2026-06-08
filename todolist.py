print("Welcome to To Do List:")
tasks=[]
while True:
  print("these are the options you have in the to do list:")
  print("1.Add task")
  print("2.View task")
  print("3.Delete Task")
  print("4.Exit")
  choice=int(input("enter your choice:"))
  if(choice==1):
    task=input("enter task:")
    tasks.append(task)
    print("Task added successfully")
  elif(choice ==2):
     print("All tasks are:")
     for i,task in enumerate( tasks,start=1):
       print(i,task)
  elif(choice==3):
     poptask=int(input("enetr task num:"))
     tasks.pop(poptask-1)
     print("Task Deleted ")
  elif(choice ==4):
    print("Thanks for using ! Have a great Day")
    break
  else:
    print("Invalid Choice")
    break