# Submitted by Brent Ingle June 9, 2014

# -------------------------------- #
# Intro to CS Final Project        #
# Gaming Social Network [Option 1] #
# -------------------------------- #
#
# For students who have paid for the full course experience:
# please check submission instructions in the Instructor Note below.
# ----------------------------------------------------------------------------- 

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <username> is connected to <name1>, <name2>,...,<nameN>. 
# <username> likes to play <game1>,...,<gameN>.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a gamer profile. For example:
# 
# John is connected to Bryant, Debra, Walter. 
# John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two - (e.g. lists of dictionaries). Pick one which
# will allow you to manage the data above and implement the procedures below. 
# 
# You can assume that <username> is a unique identifier for a user. In other
# words, there is only one John in the network. Furthermore, connections are not
# symmetric - if John is connected with Alice, it does not mean that Alice is
# connected with John. 
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
# Some details:  Each sentence will be separated from one another with only
# a period (there will not be whitespace or new lines between sentences)
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

example_input_alternate="""John is connected to Bryant, Debra, Walter. John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner. Bryant is connected to Olive, Ollie, Freda, Mercedes. Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man. Mercedes is connected to Walter, Robin, Bryant. Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures. Olive is connected to John, Ollie. Olive likes to play The Legend of Corgi, Starfleet Commander. Debra is connected to Walter, Levi, Jennie, Robin. Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords. Walter is connected to John, Levi, Bryant. Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man. Levi is connected to Ollie, John, Walter. Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma. Ollie is connected to Mercedes, Freda, Bryant. Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game. Jennie is connected to Levi, John, Freda, Robin. Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms. Robin is connected to Ollie. Robin likes to play Call of Arms, Dwarves and Swords. Freda is connected to Olive, John, Debra. Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."""

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information. 
# 
# Arguments: 
#   string_input: block of text containing the network information
# 
# Return: 
#   The new network data structure


# Helper function parses the block of text for use in create_data_structure
def get_gamer_info(gamer_info):
    
    connection_delimiter = " is connected to "
    game_delimiter = " likes to play "
    connection_delimiter_index = gamer_info.find(connection_delimiter)
    user_name = gamer_info[:connection_delimiter_index]
    if "." in user_name:
        user_name = user_name[1:]
    connection_string = gamer_info.find(".", connection_delimiter_index)
    connection_names = gamer_info[connection_delimiter_index + len(connection_delimiter) : connection_string].split(", ")
    game_delimiter_index = gamer_info.find(game_delimiter, connection_string)
    game_string = gamer_info.find(".", game_delimiter_index)
    game_names = gamer_info[game_delimiter_index + len(game_delimiter) : game_string].split(", ")
    return user_name, connection_names, game_names, game_string


def create_data_structure(gamer_info):
    # Creates empty dictionary that will be base of network structure
    network = {}
    # Continues to parse block of text as long as statements are True
    while True:
        # Assigns returned info from get_gamer_info to respective variable
        user_name, connection_names, game_names, game_string = get_gamer_info(gamer_info)
        # If user_name exists, creates name as key in network dict 
        # and assigns another dict with lists as values containing connections and games
        if user_name:
            network[user_name] = {"connections" : connection_names, "games" : game_names}
            # Resets gamer_info so get_gamer_info can continue to parse from last spot "game_string"
            gamer_info = gamer_info[game_string:]
        # Stops parsing when user_name is no longer True
        else:
            break
    # Returns a dictionary with dictionaries with lists as the data structure
    return network
    

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections a user has.
#
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user:    String containing the name of the user.
# 
# Return: 
#   A list of all connections the user has. If the user has no connections, 
#   return an empty list. If the user is not in network, return None.  

def get_connections(network, user):
    # Checks is user is in network
    if user not in network:
        return None
    # Returns an empty list if user does not have connections
    elif network[user]["connections"] == []:
        return []
    else:
        # Returns user's connections if they exist
        return network[user]["connections"]

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user_A:  String with the name of the user ("Gary")
#   user_B:  String with the name of the user that will be the new connection.
#
# Return: 
#   The updated network with the new connection added (if necessary), or False 
#   if user_A or user_B do not exist in network.

def add_connection(network, user_A, user_B):
    # Checks is users are in network
    if user_A not in network or user_B not in network:
        return False
    else:
        # Appends user_B to user_A's connections if not there already
        if user_B not in network[user_A]["connections"]:
            network[user_A]["connections"].append(user_B)
            return network
        else:
            # Does nothing if user_B is already in user_A's connections
            return network

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: The network you created with create_data_structure. 
#   user:    String containing the users name to be added (e.g. "Dave")
#   games:   List containing the user's favorite games, e.g.:
#            ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. If the 
#   user is already in the network, update their game preferences as necessary.

# Helper function used join two lists into one without repeating items
# Union is used in functions add_new_user and get_secondary_connections
def union(first_list, second_list):
    # Checks if second_list exists in network
    if not second_list:
        return
    # Iterates through each item in a list and appends the first_list if item not there
    for item in second_list:
        if item not in first_list:
            first_list.append(item)

def add_new_user(network, user, games):
    # If user doesn't exist, adds user with games and an empty connection list
    if user not in network:
        network[user] = {"connections" : [], "games" : games}
    # Does nothing to network if user already exits and games list argument is empty
    elif user in network and games == []:
        return "User %s already exists and no games were added to their profile." % user
    else:
        # Uses union helper function if user exists and games not in users list
        union(network[user]["games"], games)
    return network

# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections, i.e. connections of connections, of a 
#   given user.
# 
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user:    String containing the name of a user.
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   If the user is not in the network, return None. If a user has no primary 
#   connections to begin with, you should return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.

def get_secondary_connections(network, user):
    # Creates list used to store a user's secondary connections
    secondary = []
    # Checks if user is in network
    if user not in network:
        return False
    # Checks if user has no connections and returns the user's empty connection list
    elif network[user]["connections"] == []:
        return []
    else:
        # Iterates through user's connections and uses union helper function to
        # append connections of the user's connections to secondary list
        for connection in network[user]["connections"]:
                union(secondary, network[connection]["connections"])
    return secondary   

# -----------------------------------------------------------------------------     
# connections_in_common(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user_A:    String containing the name of user_A.
#   user_B:    String containing the name of user_B.
#
# Return: 
#   The number of connections in common (integer). Should return False if 
#   user_A or user_B are not in network.

def connections_in_common(network, user_A, user_B):
    # Creates empty list to store connections in common
    in_common = []
    # Checks if users are in network
    if user_A not in network or user_B not in network:
        return False
    else:
        # Iterates through user_A's connections and checks if they are in user_B's 
        # appends common friends to in_common list in order to get a correct count
        for friend in network[user_A]["connections"]:
            if friend in network[user_B]["connections"]:
                in_common.append(friend)
    # Returns amount of items in list in integer form
    return len(in_common)

# ----------------------------------------------------------------------------- 
# path_to_friend(network, user, connection): 
#   Finds the connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#                   Solve this problem using recursion. 
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A List showing the path from user_A to user_B. If such a path does not 
#   exist, return None
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hint: 
#   Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.

def path_to_friend(network, user, connection, path_list = []):
    # Begins by adding current user to path_list(Important for recursive action later)
    path_list = path_list + [user]
    # First base case for recursion function
    if connection in network[user]["connections"]:
        return path_list + [connection]
    # Second base case is in place if either user or connection not in network
    elif user not in network or connection not in network:
        return None
    else:
        # Iterates through current user connections
        for friend in (network[user]["connections"]):
            # Checks if friend is already in list. Continues iterating if already in path_list.
            if friend not in path_list:
                # Sets the function to variable newpath with friend as the new "user" 
                # Recursion performed here by calling itself to retrieve newpath
                newpath = path_to_friend(network, friend, connection, path_list)
                if newpath:
                    return newpath

                    
# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun!

#Defines MYOP as most_popular_game and calls for a single argument
def most_popular_game(network):
    # Assigns an empty list to store user games from network
    games_list = []
    # Assigns an empty dictionary for use later when counting recurrence of games
    game_count = {}
    # Iterates through every user in network
    for user in network:
        #  Iterates through every game in a user's game list            
        for game in network[user]["games"]:
            # Adds each game to the once empty list  
            games_list += [game]
            # Checks if game is a key in the dictionary and adds one to the value(games will not be in dict first time around)
            if game in game_count:
                game_count[game] += 1
            # Places each game in the empty dict as a key with a starting value
            else:
                game_count[game] = 1
    # Did some searching to find this solution that gets the higest value in the dict and assigns its key to the variable
    most_popular = max(game_count, key = game_count.get)

    # Returns answer in a more legible string format
    return "The most popular game is \"%s\", with %s users in common." % (most_popular, game_count[most_popular])


net = create_data_structure(example_input)
#print net
#print path_to_friend(net, 'John', 'Ollie')
#print get_connections(net, "Debra")
#print add_new_user(net, "Debra", []) 
#print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
#print get_connections(net, "Mercedes")
#print add_connection(net, "John", "Freda")
#print get_secondary_connections(net, "Mercedes")
#print connections_in_common(net, "Mercedes", "John")
#print most_popular_game(net)

