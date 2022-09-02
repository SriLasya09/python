for i in range(5):
    print(i)
    
    
for a in range(10,15):
    print(a)   
    
squares=["red", "yellow" , "green" , "purple", "blue"] 
for i in range(0,5):
    squares[i]="white"  
    print(squares)   

for x in ['A', 'B', 'C']:
    print(x+'A')  
    
square=['red','yellow','green']
for i,square in enumerate(square):
    print(i,square)   
    
    
    
#while
squares2=['orange','orange','purple','orange','blue','blue']
Newsquares=[]
i=0
while(squares2[i]=='orange'):
    Newsquares.append(squares2[i])
    i=i+1
    print(Newsquares)
      