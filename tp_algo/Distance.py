
import math


class Distance:
    
    def __init__(self):
        pass
    
    def manhattan(self, centre, noeud):
        dist=0
        if len(centre)!=len(noeud):
            print "erreur"
            return
        for i in range(len(centre)):
            dist+=math.fabs(centre[i]-noeud[i])     
        return dist
        
    def euclidienne(self, centre, noeud):
        som=0
        if len(centre)!=len(noeud):
            print "erreur"
            return
        for i in range(len(centre)):
            som+=(centre[i]-noeud[i])**2
        dist=math.sqrt(som)     
        return dist
        
    def minkowski(self, centre, noeud, p):
        som=0
        if len(centre)!=len(noeud):
            print "erreur"
            return
        for i in range(len(centre)):
            som+=(centre[i]-noeud[i])**2
        dist=math.sqrt(som)     
        return dist
        
        
        
        
