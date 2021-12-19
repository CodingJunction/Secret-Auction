import os

name=[]
price=[]
print("""

  _________                            __       _____                 __  .__               
 /   _____/ ____   ___________   _____/  |_    /  _  \  __ __   _____/  |_|__| ____   ____  
 \_____  \_/ __ \_/ ___\_  __ \_/ __ \   __\  /  /_\  \|  |  \_/ ___\   __\  |/  _ \ /    \ 
 /        \  ___/\  \___|  | \/\  ___/|  |   /    |    \  |  /\  \___|  | |  (  <_> )   |  \\
/_______  /\___  >\___  >__|    \___  >__|   \____|__  /____/  \___  >__| |__|\____/|___|  /
        \/     \/     \/            \/               \/            \/                    \/ 
""")
print('Welcome to the SECRET Auction')
print('If there are two or more bidders with same price, then first one wins')
nm = input('Enter your name\n')
name.append(nm)
bid = float(input('What is your bid ? : ₹'))
price.append(bid)
print("""Is there anyother bidder present?
Enter 'yes' for yes and
Enter 'no' for no""")
choice=input()
if choice=="yes":
  choice=True
else:
  choice=False
while choice:
 
  os.system("cls")
  nm = input('Enter your name\n')
  name.append(nm)
  bid = float(input('What is your bid ? : ₹'))
  price.append(bid)
  print("""Is there anyother bidder present?
Enter 'yes' for yes and
Enter 'no' for no""")
  choice=input()
  if choice=="yes":
    choice=True
  else:
    choice=False

maxele=max(price)
maxind=price.index(maxele)
maxnm=name[maxind]
print(f"The bid is won by {maxnm} of ₹{maxele}")




