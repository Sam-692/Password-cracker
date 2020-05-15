class User:
    """
    Class that generates new instances of user credentials
    """

    user_list = [] # Empty user list

    def __init__(self,first_name,last_name,user_name,password):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
        
    def save_account(self):

        """
        save_account method to save user accounts
        """
        User.user_list.append(self)    
