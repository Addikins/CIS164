import re


def print_emails(emails):
    print("Email addresses found: ")
    for email in emails:
        print(email)


emailstring = "Cochise College has multiple email addresses to include admissions@cochise.edu and fa@cochise.edu which are important to know!"
# As an unnecessary note, I worked in the Financial Aid office as a work study.
# The email address has been changed from fa@cochise.edu to finaid@cochise.edu.

email_regex = re.compile(r'\w*@\w*.\w*')

emails_found = email_regex.findall(emailstring)

print_emails(emails_found)
