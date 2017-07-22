+++
title = "Systems and Signals"
tags = ["mathematics", "dsp", "finance"]
categories = ["mathematics"]
description = "trying to understand systems and signals"
menu = ""
banner = ""
images = []
date = "2017-01-14T18:51:13-05:00"
draft = true
+++

## Preface

attempt to summarize and develop an intuition for lectures
[one](https://youtu.be/hVOA8VtKLgk),
[two](https://youtu.be/yIYcT7U2OaA) and
[three](https://youtu.be/kVSUnbgul7g).

## What is a signal?

In the signal processing literature, there is (at least from my experience)
always a distinction made between <em>systems</em> and <em>signals</em>.
<em>signals</em> are a kind of 'primitive type' and are characterized as
functions from a domain to some codomain. In 'classical' signals processing
the domain is continuous and is generally represented with the set $\mathbb{R}$.
In DSP the domain is discrete and generally represented with the
set $\mathbb{Z}$. In contrast, <em>systems</em> are presented as 'higher order'
functions that <em>operate on</em> signals. A basic and widely applicable system
is the <strong>lowpass filter</strong>. The 'hello world' implementation of a
lowpass filter is a N-point <strong>moving average</strong>. We'll restrict
ourselves the DSP for now. The following is a 'system level' implementation of
a 3-point moving average:

$$
y[n] = \frac{1}{3}x[n] + \frac{1}{3}x[n-1] + \frac{1}{3}x[n-2]
$$

given a system like this, we can ask how it transforms (or responds to) the
delta function:

<p>

$$
\delta[n] =
\begin{cases}
  1 & n = 0 \\
  0 & n \neq 0
\end{cases}
$$

</p>

If we substitute $\delta$ into the LHS of the 3-point moving average we get
the following ($y$ is renamed to $h$)

<p>

$$
h[n] =
  \begin{cases}
    \frac{1}{3} & n = 0 \\
    \frac{1}{3} & n = 1 \\
    \frac{1}{3} & n = 2 \\
    0 & otherwise
  \end{cases}
$$

</p>

The 3-point moving average is LTI, so it can be completely characterized by its
input signal convolved with $h$. This property allows us to implement a simple
moving average in an elegant way (performance of the implementation is a different story).

```python
# input signal
x = np.array(...)
# impulse response
h = np.full((3,), 1 / 3.)
# output signal
y = np.convolve(x, h, mode='valid');
```
