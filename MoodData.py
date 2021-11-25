import pickle

#too use this file: from MoodData import close_pkl,add_data
mood_dict = {
    "woof" : "giig",
    "hello" : "yes"
}
# reading from pickle file
def create_pkl_file ():
    mood_dict = {
    "date time" : "moodstate"
    }

    filename = 'mood.pkl'
    outfile = open(filename,'wb') # 'wb' means write binary
    pickle.dump(mood_dict,outfile)
    outfile.close()
    # reading from pickle file
    infile = open(filename,'rb')
    data = pickle.load(infile)
    infile.close()

filename = 'mood.pkl'
infile = open(filename,'rb')
mood_dict = pickle.load(infile)
print (f"mood dict opened as \n {mood_dict}")

#changing the data from the picklefile. Call this function to add info as dict strings. 
def add_data (time_stamp, data):
    new_info = {time_stamp: data}
    mood_dict.update(new_info)
    print (f"mood dict saved as \n {mood_dict}")

#this dumps and closes the pkl file. Call this at the end of the program
def close_pkl ():
    outfile = open(filename,'wb') # 'wb' means write binary
    pickle.dump(mood_dict,outfile)
    print (f"mood dict saved as \n {mood_dict}")
    outfile.close()

