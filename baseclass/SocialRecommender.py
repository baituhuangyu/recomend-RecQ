from baseclass.IterativeRecommender import IterativeRecommender
from data.social import SocialDAO
from tool import config
from os.path import abspath
class SocialRecommender(IterativeRecommender):
    def __init__(self,conf,trainingSet=None,testSet=None,relation=list(),fold='[1]'):
        super(SocialRecommender, self).__init__(conf,trainingSet,testSet,fold)
        self.social = SocialDAO(self.config,relation) #social relations access control

        # data clean
        cleanList = []
        cleanPair = []
        for user in self.social.followees:
            if user not in self.data.user:
                cleanList.append(user)
            for u2 in self.social.followees[user]:
                if u2 not in self.data.user:
                    cleanPair.append((user, u2))
        for u in cleanList:
            del self.social.followees[u]

        for pair in cleanPair:
            if pair[0] in self.social.followees:
                del self.social.followees[pair[0]][pair[1]]

        cleanList = []
        cleanPair = []
        for user in self.social.followers:
            if user not in self.data.user:
                cleanList.append(user)
            for u2 in self.social.followers[user]:
                if u2 not in self.data.user:
                    cleanPair.append((user, u2))
        for u in cleanList:
            del self.social.followers[u]

        for pair in cleanPair:
            if pair[0] in self.social.followers:
                del self.social.followers[pair[0]][pair[1]]

    def readConfiguration(self):
        super(SocialRecommender, self).readConfiguration()
        regular = config.LineConfig(self.config['reg.lambda'])
        self.regS = float(regular['-s'])

    def printAlgorConfig(self):
        super(SocialRecommender, self).printAlgorConfig()
        print('Social dataset:',abspath(self.config['social']))
        print('Social size ','(User count:',len(self.social.user),'Trust statement count:'+str(len(self.social.relation))+')')
        print('Social Regularization parameter: regS %.3f' % (self.regS))
        print('=' * 80)

