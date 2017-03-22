# -*- coding: utf-8 -*-

import random
import sys
from Distance import Distance

def read_data(filename, skip_first_line = False, ignore_first_column = False):
    '''
    Loads data from a csv file and returns the corresponding list.
    All data are expected to be floats, except in the first column.
    
    @param filename: csv file name.
    
    @param skip_first_line: if True, the first line is not read.
        Default value: False.
    
    @param ignore_first_column: if True, the first column is ignored.
        Default value: False.
    
    @return: a list of lists, each list being a row in the data file.
        Rows are returned in the same order as in the file.
        They contains floats, except for the 1st element which is a string
        when the first column is not ignored.
    '''
    
    f = open(filename,'r')
    if skip_first_line:
        f.readline()
    
    data = []
    i=0
    for line in f:
        line = line.split(",")
        del line[-1]
        line = [ float(x) for x in line ]
        i+=1
        line.insert(0,i)
        if ignore_first_column:
            line = line[1:]
        data.append(line)
    f.close()
    return data



def write_data(data, filename):
    '''
    Writes data in a csv file.

    @param data: a list of lists

    @param filename: the path of the file in which data is written.
        The file is created if necessary; if it exists, it is overwritten.
    '''
    # If you're curious, look at python's module csv instead, which offers
    # more powerful means to write (and read!) csv files.
    f = open(filename, 'w')
    for item in data:
        f.write(','.join([repr(x) for x in item]))
        f.write('\n')
    f.close()

def generate_random_data(nb_objs, nb_attrs, frand = random.random):
    '''
    Generates a matrix of random data.
    
    @param frand: the fonction used to generate random values.
        It defaults to random.random.
        Example::

            import random
            generate_random_data(5, 6, lambda: random.gauss(0, 1))
    
    @return: a matrix with nb_objs rows and nb_attrs+1 columns. The 1st
        column is filled with line numbers (integers, from 1 to nb_objs).
    '''
    data = []
    for i in range(nb_objs):
        #line = [i+1]
        #for j in range(numAtt):
        #    line.append(frand())
        line = [i+1] + map(lambda x: frand(), range(nb_attrs))
        data.append(line)
    return(data)
    
def initialise(data,k):
    centres = []
    index = []
    i=0    
    while(len(centres) != k):
        j = random.randint(0,len(data)-1)
        if j not in index :
 #           
  #          data[j][0]=i
            centres.append(data[j])
            centres[i][0]=i+1
            i+=1
            index.append(j)
            
    return centres


def calculerDistance(centres,graph, distance):# calcul de la distance
    distances = []
    dList=[]
    
    if distance=="euclidienne":
        for j in range(len(graph)):   
            dList=[] 
            for k in range(len(centres)):
                centre = centres[k]
                dList.append((k+1,Distance().euclidienne(centre,graph[j])))
           
            distances.append(dList)
    if distance=="manhattan":
        for j in range(len(graph)):   
             
            for k in range(len(centres)):
                centre = centres[k]
                dList.append((k+1,Distance().manhattan(centre,graph[j])))
                
            distances.append(dList)
    if distance=="minkowski":
        for j in range(len(graph)):   
             
            for k in range(len(centres)):
                centre = centres[k]
                dList.append((k+1,Distance().minkowski(centre,graph[j])))
                
            distances.append(dList)
    return distances
        
def affectClass(distances):
    triDistances=[]
    classe=[]
    for i in range(len(distances)):
        triDistances.append(sorted(distances[i], key=lambda dist:dist[1]))
    
    for dist in triDistances:
        classe.append(dist[0][0]) 
    return classe

def nouveauCentres(data,centres,classe):
    newCenter=[]
    print "gggggggggroupppppppe"
    for k in range(1,len(centres)+1):
        groupe=[]
        for i in range(len(classe)):
            if classe[i]==k:
                groupe.append(data[i])
        print groupe        
        newCenter.append(Distance().barycentre(groupe))
        newCenter[k-1][0]=k
    return newCenter
    
def final():

    classe=affectClass("euclidienne")
    centres=nouveauCentres(data,centres,classe)
    calculerDistance(centres,graph, distance)

    if nouveauCentres= ancienCentre:
        return arret
    else:
        final()



# Exemples d'utilisation

# D'abord on génère des données aléatoires

data = generate_random_data(3,2)
print "ddddddddddaaaaaaaaaaaataaaaaaaaaaaaaa"
print data
#data=read_data("data_iris.csv")
#print "data généreé++++++++++++++++++++++++++++++++++++++++++"



# Ensuite on ecrit ces donnees dans un fichier

write_data(data, "out.csv")

# Puis on relit ces donnees a partir du fichier

#data_read = read_data("Iris-setosa.csv")

# Et on affiche les 2 jeux de donnees ainsi obtenus

#print(data)

#print(data_read)
   
    
# this funtion can calculate the distance between each centre and each point.
# formule de donnee {no_observation:{no_centre: distance}}
####### TEST calculerDistance and initialise ######################################
centres=initialise(data, 3)
print "ccccceeeeeeeeeeeeeeeeeennnnnntrrrrreee"
print centres

m =nouveauCentres(data,centres,affectClass(calculerDistance(centres,data, "euclidienne")))
print "ccccccccllllassssssse"
print affectClass(calculerDistance(centres,data, "euclidienne"))
#print calculerDistance(centres,data, "euclidienne")
print "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
print(m)

###################################################################################






















































