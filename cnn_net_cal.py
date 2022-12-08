"""_summary_




n_out = [(n_in + 2p -k)/s] + 1

where, 
n_out = No. output feature
n_in = No. input feature
p = convolution padding size
k = Convolution kernel size
s = Convolution stride size
"""

n_out = None
n_in = 150
p = 1
k = 3
s = 1

n_out = (((n_in + 2*p) - k)/s) + 1
print(f'n_out : {n_out}')
