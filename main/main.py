import sys
sys.path.append("..")
from RecQ import RecQ
from tool.config import Config
from visual.display import Display



if __name__ == '__main__':

    print('='*80)
    print('   RecQ: An effective python-based recommender algorithm library.   ')
    print('='*80)
    print('0. Analyze the input data.(Configure the visual.conf in config/visual first.)')
    print('-' * 80)
    print('Rating-based Recommenders:')
    print('1. UserKNN        2. ItemKNN        3. BasicMF        4. SlopeOne        5. SVD')
    print('6. PMF            7. SVD++          8. EE             9. BPR             10. WRMF')
    print('11. ExpoMF')

    print('Social Recommenders:')
    print('s1. RSTE          s2. SoRec         s3. SoReg         s4. SocialMF       s5. SBPR')
    print('s6. SREE          s7. LOCABAL       s8. SocialFD      s9. TBPR           s10. SERec')


    print('Advanced Recommenders:')
    print('a1. CoFactor      a2. CUNE-MF       a3. CUNE-BPR      a4. IF-BPR         a5. APR')

    print('Baselines:')
    print('b1. UserMean      b2. ItemMean      b3. MostPopular   b4. Rand')

    print('Deep Recommenders:')
    print('d1. CDAE          d2. DMF')

    print('='*80)
    algor = -1
    conf = -1
    order = raw_input('please enter the num of the algorithm to run it:')
    import time
    s = time.time()
    if order == '0':
        try:
            import seaborn as sns
        except ImportError:
            print('!!!To obtain nice data charts, ' \
                  'we strongly recommend you to install the third-party package <seaborn>!!!')
        conf = Config('../config/visual/visual.conf')
        Display(conf).render()
        exit(0)
    elif order == '1':
        conf = Config('../config/UserKNN.conf')

    elif order == '2':
        conf = Config('../config/ItemKNN.conf')

    elif order == '3':
        conf = Config('../config/BasicMF.conf')

    elif order == '4':
        conf = Config('../config/SlopeOne.conf')

    elif order == '5':
        conf = Config('../config/SVD.conf')

    elif order == '6':
        conf = Config('../config/PMF.conf')

    elif order == '7':
        conf = Config('../config/SVD++.conf')

    elif order == '8':
        conf = Config('../config/EE.conf')

    elif order == '9':
        conf = Config('../config/BPR.conf')

    elif order == '10':
        conf = Config('../config/WRMF.conf')

    elif order == '11':
        conf = Config('../config/ExpoMF.conf')

    elif order == 's1':
        conf = Config('../config/RSTE.conf')

    elif order == 's2':
        conf = Config('../config/SoRec.conf')

    elif order == 's3':
        conf = Config('../config/SoReg.conf')

    elif order == 's4':
        conf = Config('../config/SocialMF.conf')

    elif order == 's5':
        conf = Config('../config/SBPR.conf')

    elif order == 's6':
        conf = Config('../config/SREE.conf')

    elif order == 's7':
        conf = Config('../config/LOCABAL.conf')

    elif order == 's8':
        conf = Config('../config/SocialFD.conf')

    elif order == 's9':
        conf = Config('../config/TBPR.conf')

    elif order == 's10':
        conf = Config('../config/SERec.conf')

    elif order == 'a1':
        conf = Config('../config/CoFactor.conf')

    elif order == 'a2':
        conf = Config('../config/CUNE_MF.conf')

    elif order == 'a3':
        conf = Config('../config/CUNE_BPR.conf')

    elif order == 'a4':
        conf = Config('../config/IF_BPR.conf')

    elif order == 'a5':
        conf = Config('../config/APR.conf')

    elif order == 'b1':
        conf = Config('../config/UserMean.conf')

    elif order == 'b2':
        conf = Config('../config/ItemMean.conf')

    elif order == 'b3':
        conf = Config('../config/MostPopular.conf')

    elif order == 'b4':
        conf = Config('../config/rand.conf')

    elif order == 'd1':
        conf = Config('../config/CDAE.conf')

    elif order == 'd2':
        conf = Config('../config/DMF.conf')

    else:
        print('Error num!')
        exit(-1)
    recSys = RecQ(conf)
    recSys.execute()
    e = time.time()
    print("Run time: %f s" % (e - s))
