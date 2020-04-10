import re


websitestring = "Cochise College has multiple websites to include http://www.cochise.edu and http://my.cochise.edu which are important to know!"

website_regex = re.compile(r'http://\w*.\w+.\w+')

website_found = website_regex.search(websitestring)

print("First website found: " + website_found.group())
