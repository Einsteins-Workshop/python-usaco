# The purpose of this exercise is to keep track of movies (or books or tv shows) that you've
# rated and print out the ranked list.  You can use any numerical system you wish

RANKINGS_FILE = "my_rankings.txt"

# The storing and loading of the files are done for you here, you can skip this part or
# read it if you wish
def get_stored_rankings(file_name):
    try:
        rankings = {}
        with open(file_name, 'r') as file:
            for line in file:
                line_info = "\t".split(line.rstrip())
                rankings[line_info[0]] = rankings[line_info[1]]
        return rankings
    except IOError:
        return {}

def store_rankings(file_name, rankings):
    with open(file_name, 'w') as file:
        for key, value in rankings:
            file.write(f"{key}\t{value}\n")

# Get the stored rankings, done for you
my_rankings = get_stored_rankings(RANKINGS_FILE)

title = input("Type in a title you wish to rank, or just return if you want to view all rankings")
# Fix the loop so that the loop stops if the title is the empty string
while False:
    pass

    # Check to see if the title has already been ranked
        # If the title has already been asked, show the user the current tanking

    # Ask the user for the new ranking of the title, and store the ranking in my_rankings

    # Ask the user for another title

# Next, loop over all of my_rankings, sorted by the value.
# See https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value for help on sort.
    # In each loop, print out

# Store the rankings
store_rankings(RANKINGS_FILE, my_rankings)
