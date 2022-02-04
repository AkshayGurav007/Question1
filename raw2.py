def menu():
    print("1.server 1:")
    print("2.server 2:")
    print("3.server 3:")
    print("4.exit server")
    pick=int(input("enter choice:"))
    return pick

def sum(c):
    sum=0
    for i in c:
        sum = sum+i
    return (sum)
def sum1(c1):
    sum1=0
    for i in c1:
        sum1 = sum1+i
    return (sum1)

def main():
    choice = menu()
    while choice !=4:
        if choice ==1:
           
           num=int(input("Number Of users:-"))
           num1=int(input("Server Capacity:-"+'GB'))
           c=list(map(int,input("priority number of their for the coming week:-").strip().split()))
          
           print("Total value added by all project fo a week:" +str(sum(c)))
         
           c1=list(map(int,input("RAM Usage of task(in GB):-").strip().split()))
           print("Total value added by task:" +str(sum1(c1)))
        elif choice == 2:
            num=int(input("Number Of users:-"))
            num1=int(input("Server Capacity:-"+'GB'))
            c=list(map(int,input("priority number of their for the coming week:-").strip().split()))
          
            print("Total value added by all project fo a week:" +str(sum(c)))
         
            c1=list(map(int,input("RAM Usage of task(in GB):-").strip().split()))
            print("Total value added by task:" +str(sum1(c1)))
        elif choice == 3:
            num=int(input("Number Of users:-"))
            num1=int(input("Server Capacity:-"+'GB'))
            c=list(map(int,input("priority number of their for the coming week:-").strip().split()))
          
            print("Total value added by all project fo a week:" +str(sum(c)))
         
            c1=list(map(int,input("RAM Usage of task(in GB):-").strip().split()))
            print("Total value added by task:" +str(sum1(c1)))
        else:
             print("invalid entry")
             choice==menu()
        

      

menu()
main()
