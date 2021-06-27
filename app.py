#==========================================#
# Developed by :   github.com/rohit-chouhan
# License      :   MIT 
# Last Update  :   June 27, 2021
#==========================================#
import requests

def follow(t):
    page = 1
    indexing = 0
    limit=int(input("\n Enter Follow Limit: "))
    user=int(input(" Enter The User name of Person to Follow their Followers: "))
    for i in range(limit):
        response = requests.get('https://api.github.com/users/'+user+'/followers?page='+str(page), headers= {'Authorization' : 'Bearer '+t+''})
        res = response.json()
        requests.put('https://api.github.com/user/following/'+res[indexing]['login'], headers= {'Authorization' : 'Bearer '+t+''})
        print(" ("+str(i+1)+") Followed User Successfully: @"+res[indexing]['login'])
        if indexing==29:
            page+=1
            indexing=0
        elif i==limit:
            break
        else:
            pass
        indexing+=1   

    print("\n\n===== Task Complete Successfully =====")
    print("\n\nNote: Github takes 5-10min to update!")
    
def unfollow(u,t):
    page = 1
    indexing = 0
    limit=int(input("\n Enter UnFollow Limit: "))
    for i in range(limit):
        response = requests.get('https://api.github.com/users/'+u+'/following?page='+str(page), headers= {'Authorization' : 'Bearer '+t+''})
        res = response.json()
        requests.delete('https://api.github.com/user/following/'+res[indexing]['login'], headers= {'Authorization' : 'Bearer '+t+''})
        print(" ("+str(i+1)+") Unfollowed User Successfully: @"+res[indexing]['login'])
        if indexing==29:
            page+=1
            indexing=0
        elif i==limit:
            break
        else:
            pass
        indexing+=1   

    print("\n\n===== Task Complete Successfully =====")
    print("\n\nNote: Github takes 5-10min to update!")

print("============Github Tool by @rohit-chouhan =============")

username=input("Your Username: ")
usertoken=input("Your Token: ")

print("\n\n========= Tools ===========")
print("1.Follow\n2.Unfollow")
ans = input("\nYour Choice: ")

if ans=="1":
    follow(usertoken)
else:
    unfollow(username,usertoken)
