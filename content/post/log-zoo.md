+++
tags = []
categories = []
description = ""
menu = ""
banner = ""
date = "2017-07-05T10:55:51-04:00"
title = "log zoo"
images = []
draft = true
+++

# Preface

keeping track of logs.

the exponential turn sums into products.

<p>

$$

e^{a+b}=e^a\cdot e^b

$$

</p>

the logarithm (shown here with base $e$) transforms products into sums.

<p>

$$

\ln(ab)=\ln(a)+\ln(b)

$$

</p>

# The Logistic Function

$$

f(x) = \frac{L}{1 + e^{-k(x-x_0)}}

$$

# The 'Standard' Logistic Function

$$

s(x) = \frac{1}{1 + e^{-k}}

$$

# The Logit Function

$$

logit(p) = ln(\frac{p}{1-p})

$$

# The Softplus Function

$$

softplus(x) = ln(e^{x} + 1)

$$

## note

$$

logit^{-1} = s = \frac{d}{dx}softplus

$$

# Question

* whats with this inverse?
* is this an example of an exponential response model?
* the logit function is the canonical link function for
the Bernoulli distribution
https://en.wikipedia.org/wiki/Generalized_linear_model#Identity_link
https://en.wikipedia.org/wiki/Score_(statistics)
