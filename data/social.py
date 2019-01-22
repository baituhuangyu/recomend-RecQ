import numpy as np
from structure import sparseMatrix,new_sparseMatrix
from tool.config import Config,LineConfig
from tool.qmath import normalize
import os.path
from re import split

class SocialDAO(object):
    def __init__(self,conf,relation=list()):
        self.config = conf
        self.user = {} #used to store the order of users
        self.relation = relation
        self.followees = {}
        self.followers = {}
        self.trustMatrix = self.__generateSet()

    def __generateSet(self):
        triple = []
        for line in self.relation:
            userId1,userId2,weight = line
            #add relations to dict
            if userId1 not in self.followees:
                self.followees[userId1] = {}
            self.followees[userId1][userId2] = weight
            if userId2 not in self.followers:
                self.followers[userId2] = {}
            self.followers[userId2][userId1] = weight
            # order the user
            if userId1 not in self.user:
                self.user[userId1] = len(self.user)
            if userId2 not in self.user:
                self.user[userId2] = len(self.user)
            triple.append([self.user[userId1], self.user[userId2], weight])
        return new_sparseMatrix.SparseMatrix(triple)

    def row(self,u):
        #return user u's followees
        return self.trustMatrix.row(self.user[u])

    def col(self,u):
        #return user u's followers
        return self.trustMatrix.col(self.user[u])

    def elem(self,u1,u2):
        return self.trustMatrix.elem(u1,u2)

    def weight(self,u1,u2):
        if u1 in self.followees and u2 in self.followees[u1]:
            return self.followees[u1][u2]
        else:
            return 0

    def trustSize(self):
        return self.trustMatrix.size

    def getFollowers(self,u):
        if u in self.followers:
            return self.followers[u]
        else:
            return {}

    def getFollowees(self,u):
        if u in self.followees:
            return self.followees[u]
        else:
            return {}

    def hasFollowee(self,u1,u2):
        if u1 in self.followees:
            if u2 in self.followees[u1]:
                return True
            else:
                return False
        return False

    def hasFollower(self,u1,u2):
        if u1 in self.followers:
            if u2 in self.followers[u1]:
                return True
            else:
                return False
        return False
