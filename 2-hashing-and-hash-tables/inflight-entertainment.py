# Write a function that takes an integer flight_length (in minutes) 
# and a list of integers movie_lengths (in minutes) 
# and returns a boolean indicating whether there are two numbers 
# in movie_lengths whose sum equals flight_length.

def inflight_movie(flight_length, movie_lengths): 

    movie_dict = {}

    #Create dictionary
    for movie_length in movie_lengths:
        if movie_length not in movie_dict:
            movie_dict[movie_length] = 1
        else:
            movie_dict[movie_length] += 1

    #Check movies:
    for movie_length in movie_lengths:
        remaining_time = flight_length - movie_length
        if remaining_time == movie_length and movie_dict[remaining_time] > 1:
            return True
        elif remaining_time in movie_dict:
            return True
    return False




