import numpy as np
from scipy.stats import multivariate_normal
from scipy.stats import multinomial
import matplotlib.pyplot as plt

def rotation_matrix(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])

def sample_marginal_p_x(components=None, pis=None, num_samples=1000):
    """ sample from the marginal over x
    """
    accum = []
    for i in range(num_samples):
        # take one sample from p_pi
        sample_p_pi = np.argmax(pis.rvs(1))
        # pick component using sampled p_pi
        sample_component = components[sample_p_pi].rvs()
        accum.append(sample_component)
    return np.array(accum)


def sample_post_p_z_given_x(observed=None, components=None, pis=None):
    num_samples = observed.shape[0]
    responsibilities = []
    for i in range(num_samples):
        x_sample = observed[i,:]
        # compute evidence term (denominator of bayes rule)
        evidence = pis.pmf([1,0,0]) * components[0].pdf(x_sample) + \
                   pis.pmf([0,1,0]) * components[1].pdf(x_sample) + \
                   pis.pmf([0,0,1]) * components[2].pdf(x_sample)
        p_z_is_1_given_x = (pis.pmf([1,0,0]) * components[0].pdf(x_sample)) / float(evidence)
        p_z_is_2_given_x = (pis.pmf([0,1,0]) * components[1].pdf(x_sample)) / float(evidence)
        p_z_is_3_given_x = (pis.pmf([0,0,1]) * components[2].pdf(x_sample)) / float(evidence)
        responsibilities.append((p_z_is_1_given_x, p_z_is_2_given_x, p_z_is_3_given_x))
    return responsibilities


""" MIXTURE COMPONENTS
define three (K = 3) mixture components.
each mixture component has its own mean vector and
covariance matrix
"""

def mixture_component_1():
    mu_1 = np.array([2.,5.])
    sig_1 = np.array([
        [1., 0.],
        [0., 3.]
    ])
    return multivariate_normal(mean=mu_1, cov=sig_1)

def mixture_component_2():
    mu_2 = np.array([4., 8.])
    A2 = np.array([
        [ 2.0, -1.0 ],
        [ 2.0,  1.0 ]
    ])
    # build a matrix that rotates vectors in R^2 by 45 degress
    R = rotation_matrix(5.53269)
    sig_2_diag = np.array([
        [ np.linalg.norm([2.0, 2.0]),                        0.0  ],
        [                        0.0, np.linalg.norm([-1.0, 1.0]) ]
    ])
    sig_2 = np.dot(R.T, np.dot(sig_2_diag, R))
    return multivariate_normal(mean=mu_2, cov=sig_2)

def mixture_component_3():
    mu_3 = np.array([7.,3.])
    sig_3 = np.array([
        [2., 0.],
        [0., 2.]
    ])
    return multivariate_normal(mean=mu_3, cov=sig_3)

""" MIXTURE COEFFICIENTS
"""

pi_1 = 1/3.

pi_2 = 1/3.

pi_3 = 1/3.


pis = multinomial(1, [pi_1, pi_2, pi_3])
components = [
    mixture_component_1(),
    mixture_component_2(),
    mixture_component_3()
]

""" SAMPLE FROM MARGINAL OVER DATA
"""

def plot_sample_p_x():
    res = sample_marginal_p_x(components, pis, num_samples=10000)
    x = res[:,0]
    y = res[:,1]
    plt.axis([0,10,0,10])
    plt.scatter(x,y,s=1)

def plot_sample_post_p_z_given_x():
    # treat samples from marginal over x as new data
    # we could do this differently by sampling a 10x10 grid
    num_samples = 10000
    x_observed = sample_marginal_p_x(components, pis, num_samples)
    res = sample_post_p_z_given_x(x_observed, components, pis)
    x = x_observed[:,0]
    y = x_observed[:,1]
    plt.axis([0,10,0,10])
    plt.scatter(x,y,s=1,c=res)
