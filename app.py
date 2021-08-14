#==========================================#
# Developed by :   github.com/rohit-chouhan, github.com/7k5x
# License      :   MIT 
# Last Update  :   August 14, 2021
#==========================================#
import requests
#Using GetPass, so you should have Python 2.5 or higher
import getpass

def follow(t):
    page = 1
    indexing = 0
    limit=int(input("\n Enter Follow Limit: "))
    if not limit:
        #Person with most followers is Linus Torvalds(140k+), so 10M is more than enough
        limit=1000000
    user=str(input(" Enter The User name of Person to Follow their Followers: "))
    if not user:
        print("Please enter your username")
        exit(1)
    for i in range(limit):
        try:
            response = requests.get('https://api.github.com/users/'+user+'/followers?page='+str(page), headers= {'Authorization' : 'Bearer '+t+''})
        except:
            print("Error getting response")
        try:
            res = response.json()
        except:
            print("Error parsing JSON")
        try:
            requests.put('https://api.github.com/user/following/'+res[indexing]['login'], headers= {'Authorization' : 'Bearer '+t+''})
            print(" ("+str(i+1)+") Followed User Successfully: @"+res[indexing]['login'])
        #IndexError is caused when your limit is over the number of followers the user has, so it's not an error to worry about
        except IndexError:
            break
        except:
            print("Error following user @"+res[indexing]['login'])
        #There are 30 people(0~29) per API page index. This might change later on.
        if indexing==29:
            page+=1
            indexing=0
        elif i==limit:
            break
        else:
            pass
        indexing+=1   

    print("\n\n===== Task Completed =====")
    print("\n\nNote: Github takes 5-10min to update!")
    
def unfollow(u,t):
    page = 1
    indexing = 0
    limit=int(input("\n Enter UnFollow Limit: "))
    if not limit:
        #10M is more than enough
        limit=1000000
    for i in range(limit):
        try:
            response = requests.get('https://api.github.com/users/'+u+'/following?page='+str(page), headers= {'Authorization' : 'Bearer '+t+''})
        except:
            print("Error getting response")
        try:
            res = response.json()
        except:
            print("Error parsing JSON")
        try:
            requests.delete('https://api.github.com/user/following/'+res[indexing]['login'], headers= {'Authorization' : 'Bearer '+t+''})
            print(" ("+str(i+1)+") Unfollowed User Successfully: @"+res[indexing]['login'])
        #IndexError is caused when your limit is over the number of followers the user has, so it's not an error to worry about
        except IndexError:
            break
        except:
            print("Error unfollowing user @"+res[indexing]['login'])   
        #There are 30 people(0~29) per API page index. This might change later on.
        if indexing==29:
            page+=1
            indexing=0
        elif i==limit:
            break
        else:
            pass
        indexing+=1   

    print("\n\n===== Task Completed =====")
    print("\n\nNote: Github takes some time to update!")

print("============Github Tool by @rohit-chouhan =============")

username=input("Your Username: ")
#Use getpass for token security
usertoken=getpass.getpass('Token: ')

print("\n\n========= Tools ===========")
print("1.Follow\n2.Unfollow")
ans = input("\nYour Choice: ")

if ans=="1":
    follow(usertoken)
elif ans=="2":
    unfollow(username,usertoken)
else:
    print("Wrong input")
    exit(1)
