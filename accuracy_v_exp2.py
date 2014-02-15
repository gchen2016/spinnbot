import sys
sys.path.append('../ccmsuite')
import ccm
ccm.run('accuracy_v2', 5, N=[1000], states=['b', 'bv', 'bp', 'bvp'], S=[500,1000,1500,2000,2500,3000,3500,4000,4500,5000])