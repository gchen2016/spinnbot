import sys
sys.path.append('../ccmsuite')
import ccm
ccm.run('accuracy_v', 5, N=[10,20,50,100,200,500,1000,2000], states=['b', 'bv', 'bp', 'bvp'])