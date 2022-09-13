import csv

# csv file name
filename = "charts.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
	# creating a csv reader object
	csvreader = csv.reader(csvfile)
	
	# extracting field names through first row
	fields = next(csvreader)

	# extracting each data row one by one
	for row in csvreader:
		rows.append(row)

# printing the field names
print(' \t' + '\t\t '.join(field for field in fields))


menu_options = {
    1: 'Top ranked song for a particular day',
    2: 'Details of artist with the most top ranked songs ',

    3: 'Details of the songs with longest numbr of weeks',
    4: 'Visualize the top songs',
    5: 'Exit'
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
    #Retrieve the details for the top ranked song for a particular day	
    rows_srt = sorted(rows[1:], reverse=True, key=lambda x: x[5])
    # create new list for our subset
    rank = []
    # append first item from sorted list
    for row in rows_srt[:1]:
        for col in row:
            print("%10s"%col,end=""),
        print('\n')
    
def option2():
    #Retrieve the details of the artist with the most top ranked songs    
    rows_srt = sorted(rows[1:], reverse=True, key=lambda x: x[3])
    # create new list for our subset
    rank = []
    # append 5 first from sorted list
    for row in rows_srt[:5]:
        rank.append(row)
        for col in row:
            print("%10s"%col,end=" "),
        print('\n')
    return rank

def option3():
    #  Retrieve the details of the 10 songs with the longest number of weeks on the board
    rows_srt = sorted(rows[1:], reverse=True, key=lambda x: x[6])
    rank = []
    for row in rows_srt[:10]:
        # parsing each column of a row
        for col in row:
            print("%10s"%col,end=" \t"),
        print('\n')

def option4():
    #Visualise the top songs (the criteria for ‘top’ is up to you)
    import matplotlib.pyplot as plt
    top_songs = []
    rank = option2()
    for row in range(1, len(rank)):
        top_songs.append(rank[row][0])
    plt.grid()
    plt.barh(top_songs, width= 0.1)
    plt.title('the top songs')
    plt.xlabel('in percent')
    plt.xlabel('in percent')
    plt.show()
if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')

	






