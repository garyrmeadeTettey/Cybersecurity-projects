import subprocess

# Output for "netsh wlan show profiles" & split string into new lines
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
#Fetches all strings and adds semi-colon betwen them and strips first and last character
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
#Again loops through profiles and output specific profile 
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    #While still looping, looks for lines that contain "Key content" & spikts with semi-colon & removes first and last character
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    #should print simple list with a string with profile details
    try:
        print ("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(i, ""))
        
#The input call is to ensure that the program runs until a keyboard input, so program doesnt end immidiately.
input("")
