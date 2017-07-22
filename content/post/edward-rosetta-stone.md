+++
categories = []
description = ""
date = "2017-06-26T11:06:35-04:00"
title = "edward rosetta stone"
menu = ""
banner = ""
images = []
tags = []
draft = true
+++

# Models

In Edward, we specify models using a simple language of random variables.
A random variable $\mathbf{x}$ is an object parameterized by tensors $\theta^\ast$,
where __the number of random variables in one object is determined by the dimensions
of its parameters__.

# Univariate Normal

```python
from edward.models import Normal
uvn = Normal(loc=tf.constant(0.0), scale=tf.constant(1.0))
```

# Multivariate Normal

```python
import tensorflow as tf
from edward.models import MultivariateNormalTriL
mu = [1., 2, 3]
cov = [[ 0.36,  0.12,  0.06],
       [ 0.12,  0.29, -0.13],
       [ 0.06, -0.13,  0.26]]
scale = tf.cholesky(cov)
mvn = ds.MultivariateNormalTriL(
    loc=mu,
    scale_tril=scale)
```
