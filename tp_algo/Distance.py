import copy
import math


class Distance:
    
    def __init__(self):
        pass
    
    def barycentre(self, data):
        bary=copy.deepcopy(data[0])
        if len(data)>1:
            for noeud in data[1:]:
                for i in range(len(noeud)-1):
                    bary[i+1]+=noeud[i+1]
            for i in range(1,len(bary)):
                bary[i]=float(bary[i])/len(data)
        return bary

    
    def manhattan(self, centre, noeud):
        dist=0
        if len(centre)!=len(noeud):
            print "erreur"
            return
        for i in range(len(centre)-1):
            dist+=math.fabs(centre[i+1]-noeud[i+1])    
        return dist
        
    def euclidienne(self, centre, noeud):
        som=0
        if len(centre)!=len(noeud):
            print "erreur"
            return
        for i in range(len(centre)-1):
            som+=(centre[i+1]-noeud[i+1])**2
        dist=math.sqrt(som)     
        return dist
        
    def minkowski(self, centre, noeud, p):
        som=0
        if len(centre)!=len(noeud):
            print "erreur"
            return
        for i in range(len(centre)-1):
            som+=(centre[i+1]-noeud[i+1])**2
        dist=math.sqrt(som)     
        return dist
        
        
        
        
