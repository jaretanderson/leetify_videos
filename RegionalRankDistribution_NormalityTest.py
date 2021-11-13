# adapted from: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.normaltest.html
import numpy as np
from scipy import stats         # give access to normaltest method

# regional rank distribution datasets (aggregated from https://blog.leetify.com/state-of-csgo-july-2021/)
#   first list element is percentage of players that are silver 1 in the region, 
#   ranging up in rank order to the last element being percentage of players that are global in the region
a = [0.90,3.14,3.80,5.06,6.60,8.17,9.56,10.39,10.60,9.98,8.76,7.16,5.50,3.89,2.55,2.27,1.27,0.42]     # asian distribution
eu = [1.15,2.40,2.40,3.07,4.19,5.48,6.66,7.78,8.83,9.20,9.21,8.76,7.81,6.62,5.39,5.80,3.81,1.44]      # european distribution
sa = [1.33,2.42,2.26,3.00,4.01,5.13,6.44,7.48,8.12,8.69,8.64,8.17,7.68,7.02,6.08,7.45,4.70,1.37]      # south american distribution
na = [8.46,13.41,8.88,7.56,7.01,6.49,6.16,6.06,6.03,5.97,5.70,4.96,4.05,3.10,2.26,2.18,1.26,0.47]     # north american distribution
oc = [4.91,15.19,13.03,11.92,10.76,9.26,8.01,6.39,5.00,3.83,3.02,2.40,1.88,1.28,1.06,0.95,0.66,0.45]  # oceanic distribution

# run the tests
k2_a, p_a = stats.normaltest(a)
k2_eu, p_eu = stats.normaltest(eu)
k2_sa, p_sa = stats.normaltest(sa)
k2_na, p_na = stats.normaltest(na)
k2_oc, p_oc = stats.normaltest(oc)

# print results
print("p_a = {:g}".format(p_a))
print("k2_a = {:g}".format(k2_a))

print("p_eu = {:g}".format(p_eu))
print("k2_eu = {:g}".format(k2_eu))

print("p_sa = {:g}".format(p_sa))
print("k2_sa = {:g}".format(k2_sa))

print("p_na = {:g}".format(p_na))
print("k2_na = {:g}".format(k2_na))

print("p_oc = {:g}".format(p_oc))
print("k2_oc = {:g}".format(k2_oc))
