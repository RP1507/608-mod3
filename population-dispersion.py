#Module 3 - Chapter 4: population-dispersion 

##Using data from Chapter 4.18 10 six sided die rolls


##Set one uses population variance and standard deviation

import statistics as stat

die_sample = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]

print(stat.pvariance(die_sample))

print(stat.pstdev(die_sample))



##Set two uses sameple variance and standard deviation (sample variance and standard deviation divide by n-1 rather than n)##

print(stat.variance(die_sample))

print(stat.stdev(die_sample))