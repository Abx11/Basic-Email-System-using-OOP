### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

    # Declare the class variable, with default value, for emails. 
 
    # Initialise the instance variables for emails.


class Email:
   
   inbox = []
   
   def __init__(self, address, subject, message ):
      self.address = address
      self.subject = subject
      self.message = message
      self.mark_as_read = False
    # Create the method to change 'has_been_read' emails from False to True.
   def mark_as_read(self):
       self.mark_as_read = True
# --- Lists --- #
# Initialise an empty list to store the email objects.
# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox(email):
   Email.inbox.append(email)
   
   # Create 3 sample emails and add it to the Inbox list. 

def list_emails():
   print('Email list:')
   key = -1
   for email in Email.inbox:
      key += 1
      print(f'{key}: {email.subject}')

def unread_emails():
   print('Unread emails')
   key = -1
   for email in Email.inbox:
      key += 1
      if email.mark_as_read == False:
         print(f'{key}: {email.subject}')
   
   
   # Create a function which prints the email’s subject_line, along with a corresponding number.

def read_email(index):
    list_emails()
    index = int(input('Enter the email number you would like to read (index starts at 0): '))
    if 0 <= index < len(Email.inbox):
        email = Email.inbox[index]
        email.mark_as_read = True
        print(f'''
              =====================
              {index}:
              Email address: {email.address}
              Subject line: {email.subject}
              Message: {email.message}
              Has been read: {email.mark_as_read}
              =====================
              ''')
    else:
        print("Invalid email index.")
      
      # Create a function which displays a selected email. 
      # Once displayed, call the class method to set its 'has_been_read' variable to True.

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
email1 = Email('zoom@hyperion.com', 'Welcome to HyperionDev!', 'Nice to meet you' )
email2 = Email('fasttrack@hyperion.com', 'Great work on the bootcamp!', 'You are doing so well learning')
email3 = Email('flash@hyperion.com', 'Your excellent marks!', 'You scored 100%')

populate_inbox(email1)
populate_inbox(email2)
populate_inbox(email3)
# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        read_email(0)
        
    elif user_choice == 2:
        # add logic here to view unread emails
      # Email.list_emails()
      unread_emails()   
    elif user_choice == 3:
       print('Goodbye!')
       exit()
        # add logic here to quit application

    else:
        print("Oops - incorrect input.")
