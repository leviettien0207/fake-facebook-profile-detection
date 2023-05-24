crawl user id from group members
<br>&emsp;PROBLEM: 
<br>&emsp;&emsp;Find user by username restricts 600 results.
<br>&emsp;&emsp;Find user by recently joined restricts 1000 results.
<br>&emsp;&emsp;Compare 2 above options may leads to duplication problem.
<br>&emsp;INPUT:
<br>&emsp;&emsp;group_list (text): contains group links
<br>&emsp;&emsp;name_list(text): contains names in order to help get more user id
<br>&emsp;OUTPUT:
<br>&emsp;&emsp;id_list(text): contains user ids (could be several files)
<br>&emsp;USAGE:
<br>&emsp;&emsp;add facebook member url (exp: https://www.facebook.com/groups/machinelearningcoban/members) which fb account can access at in\group.txt
<br>&emsp;&emsp;fix names at in\str_name.txt
<br>&emsp;&emsp;python main.py
<br>
<br>crawl user info from user id