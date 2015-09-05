# Python script for use Moodle API.
# In this case the code allows to get enrrolled users in a iMOOC course

# Required libraries for use this code
#    - Python JSON library
#    - Python Requests library http://docs.python-requests.org/en/latest/

# The required parameters are:
#    - The course ID -> variable courseid
#    - The admin (or manager) token for access to Moodle services -> variable wstoken

import requests, json

parameters = {'wsfunction': core_enrol_get_enrolled_users', 'courseid':'id', 'moodlewsrestformat':'json', 'wstoken':'xxxxxx'}
url = "http://gridlab.upm.es/imooc/"

response = requests.get(url, params=parameters)

if response.status_code == 200:
    results = response.json()
    for result in results:
        print result
else:
    print "Error code %s" % response.status_code
