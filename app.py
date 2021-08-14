#==========================================#
# Developed by :   github.com/rohit-chouhan, github.com/7k5x
# License      :   MIT 
# Last Update  :   August 14, 2021
#==========================================#
import requests
#Using GetPass, so you should have Python 2.5 or higher
import getpass



#KeyboardInterrupt in loop means Ctrl+C

def follow(t):
    page = 1
    indexing = 0
    try:
        limit=int(input("\n Enter Follow Limit: "))
    except ValueError:
        limit=1000000
    except:
        exit(1)
    try:
        user=str(input(" Enter The User name of Person to Follow their Followers: "))
    except:
        print("Please enter your username")
        exit(1)
    for i in range(limit):
        try:
            response = requests.get('https://api.github.com/users/'+user+'/followers?page='+str(page), headers= {'Authorization' : 'Bearer '+t+''})
        except KeyboardInterrupt:
            print('\n')
            exit(0)
        except:
            print("Error getting response")
        try:
            res = response.json()
        except KeyboardInterrupt:
            print('\n')
            exit(0)
        except:
            print("Error parsing JSON")
        try:
            requests.put('https://api.github.com/user/following/'+res[indexing]['login'], headers= {'Authorization' : 'Bearer '+t+''})
            print(" ("+str(i+1)+") Followed User Successfully: @"+res[indexing]['login'])
        #IndexError is caused when your limit is over the number of followers the user has, so it's not an error to worry about
        except IndexError:
            break
        except KeyboardInterrupt:
            print('\n')
            exit(0)
        except:
            try:
                print("Error following user @"+res[indexing]['login'])
            except:
                print("Error following user "+str(i+1))
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
    try:
        limit=int(input("\n Enter UnFollow Limit: "))
    except ValueError:
        #10M is more than enough
        limit=1000000
    except:
        exit(1)
    for i in range(limit):
        try:
            response = requests.get('https://api.github.com/users/'+u+'/following?page='+str(page), headers= {'Authorization' : 'Bearer '+t+''})
        except KeyboardInterrupt:
            print('\n')
            exit(0)
        except:
            print("Error getting response")
        try:
            res = response.json()
        except KeyboardInterrupt:
            print('\n')
            exit(0)
        except:
            print("Error parsing JSON")
        try:
            requests.delete('https://api.github.com/user/following/'+res[indexing]['login'], headers= {'Authorization' : 'Bearer '+t+''})
            print(" ("+str(i+1)+") Unfollowed User Successfully: @"+res[indexing]['login'])
        #IndexError is caused when your limit is over the number of followers the user has, so it's not an error to worry about
        except KeyboardInterrupt:
            print('\n')
            exit(0)
        except IndexError:
            break
        except:
            try:
                print("Error unfollowing user @"+res[indexing]['login'])
            except:
                print("Error unfollowing user "+str(i+1))  
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

try:
    username=input("Your Username: ")
except KeyboardInterrupt:
    print('\n')
    exit(0)
except:
    print('Error in input')
    exit(1)
#Use getpass for token security
try:
    usertoken=getpass.getpass('Token: ')
except KeyboardInterrupt:
    print('\n')
    exit(0)
except:
    print('Error in input')
    
#GetPass doesn't show your stuff, so you could enter the wrong thing. This solves the problem.
if not usertoken.startswith("ghp_"):
    print('You didn\'t input a proper access token. It should start with ghp_ and should be 40 letters in length.')
    exit(1)
if len(usertoken) <= 40:
    print('You didn\'t input a proper access token. It should start with ghp_ and should be 40 letters in length.')
    exit(1)

print("\n\n========= Tools ===========")
print("1.Follow\n2.Unfollow")
try:
    ans = input("\nYour Choice: ")
except KeyboardIntterupt:
    print('\n')
    exit(0)
except:
    print('Error in input')

if ans=="1":
    follow(usertoken)
elif ans=="2":
    unfollow(username,usertoken)
else:
    print("Wrong input")
    exit(1)
