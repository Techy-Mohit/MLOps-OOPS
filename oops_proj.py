class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
        
    def menu(self):
        user_input = input("""welcome to Chatbook  !!  How would you like to proceed?
                           1. Press 1 to signup
                           2. press 2 to signin
                           3. press 3 to write a post
                           4. press 4 to message a friend
                           5 . press any other key to exit
                           """)
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.write_post()
        elif user_input == '4':
            self.message_friend()
        else:
            exit()
    def signup(self):
        email = input("Enter your email: ")
        password = input("Setup your password: ")
        self.username = email
        self.password = password
        print("Signup successful!")
        print("\n")
        self.menu()
        
    def signin(self):
        if(self.username == '' and self.password == ''):
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname = input("Enter your email: ")
            pword = input("Enter your password: ")
            if(uname == self.username and pword == self.password):
                self.loggedin = True
                print("Signin successful!")
            else:
                print("Invalid credentials, please try again.")
        print("\n")
        self.menu()
        
    def write_post(self):
        if self.loggedin:
           txt = input("Write your post: ")
           print(f"Post published: {txt}")
        else:
            print("please signin to write a post")
        print("\n")
        self.menu()
    
    def message_friend(self):
        if self.loggedin:
            friend = input("Enter your friend's name: ")
            msg = input("Enter your message: ")
            print(f"Message sent to {friend}: {msg}")
        else:
            print("please signin to write a message to your friend")
        print("\n")
        self.menu()
# obj = chatbook()