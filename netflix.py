import csv
video = input("What show or movie are you looking for? ")

ratings_path = 'Resources/netflix_ratings.csv'

#open_ratings = open(ratings_path, "r")
#with open(ratings_path) as ratings_data :

     # To do: perform analysis.
     #print(ratings_data)
#for title in  range(video) :

   # print (title,rating,'user rating score')

#else:
    #print("Sorry about this, we don't seem to have what you are looking for!")import csv

#with open(ratings_path) as c:
r = csv.DictReader(open(ratings_path))
for row in r:
    print(row['title'], row['user rating score'])
    #print(row)


#c = open(ratings_path,'r')
#print("The csv file is opened for reading:")
#print("\n")
#o = csv.reader(c)
#print("The contents of the above file is as follows:")
#for r in o:
#    print (r[title])


c.close()
