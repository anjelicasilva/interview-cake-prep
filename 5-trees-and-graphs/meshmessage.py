#Given information about active users on the network, find the shortest route for a message from one user (the sender) to another (the recipient). Return a list of users that make up this route.

# Your network information takes the form of a dictionary mapping username strings to a list of other users nearby:

# network = {
#     'Min'     : ['William', 'Jayden', 'Omar'],
#     'William' : ['Min', 'Noam'],
#     'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
#     'Ren'     : ['Jayden', 'Omar'],
#     'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
#     'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
#     'Miguel'  : ['Amelia', 'Adam', 'Liam', 'Nathan'],
#     'Noam'    : ['Nathan', 'Jayden', 'William'],
#     'Omar'    : ['Ren', 'Min', 'Scott'],
#     ...
# }