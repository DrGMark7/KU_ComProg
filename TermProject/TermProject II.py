
#------------------------------------------- IMDB HEADER -------------------------------------------
# Only 'import json' command is allowed!!!
# Failing to follow this rule, you will get zero mark :_)
import json
import time
start = time.time()
def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

# specifying the zip file name
filename = "D:\\Work\\KU_ComProgramming\\Elab09\\IMDB_movies_merged.json"

data = read_json(filename)
#------------------------------------------- IMDB HEADER -------------------------------------------


def q1():
    harrison_index , focus_movie = [],[]
    clean_movie , clean_movie2 = [],[]
    for i in range(len(data)):
        cast = data[i].get('cast')
        try:
            for j in range(len(cast)):
                if cast[j].get('name') == 'Harrison Ford':
                    harrison_index.append(i)
        except :
            pass 

    for i in harrison_index:
        focus_movie.append(data[i])

    for i in focus_movie:
        try:
            if 0 < float(i.get('ratingValue')) <= 10:
                clean_movie.append(i)
        except:
            pass

    for i in clean_movie:
        direc_name = i.get('director')
        try:
            if direc_name.get('name') != 'Steven Spielberg':
                clean_movie2.append(i)
        except:
            pass

    direc_name = []
    sorted_data = sorted(clean_movie2, key=lambda x: x['ratingValue'],reverse=True)
    for i in sorted_data[0:9]:
        direc_name.append(i.get('director').get('name'))
    for i in sorted(direc_name):
        print(i)

def q2():
    index_movie_harrison , index_movie_tommy = [],[]
    for i in range(len(data)):
        cast = data[i].get('cast')
        try:
            for j in range(len(cast)):
                if cast[j].get('name') == 'Tommy Lee Jones':
                    index_movie_tommy.append(i)
        except :
            pass 

    for i in range(len(data)):
        cast = data[i].get('cast')
        try:
            for j in range(len(cast)):
                if cast[j].get('name') == 'Harrison Ford':
                    index_movie_harrison.append(i)
        except :
            pass 


    same_movie = list(set(index_movie_harrison).intersection(set(index_movie_tommy)))[0]

    print(data[same_movie].get('name'))

#----- driver code -----
print('(1) Answer of Q1')
print('(2) Answer of Q2')
ans = input('or just press (Enter): ')
if ans == '1':
    q1()
    end = time.time()
    print(round(end-start,3))
elif ans == '2':
    q2()
    end = time.time()
    print(round(end-start,3))
else:
    print('Nothing to do..')