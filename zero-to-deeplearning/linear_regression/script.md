# Outline

1. Start by brainstorming and outlining the key points that
   you want to discuss in the video.
2. Develop a structure for the video, including an
   introduction, main points, and a conclusion.
3. Write a draft of the script, including any visuals,
   images, or clips that you plan to use.
4. Review and revise the script as necessary.
5. Practice the script and make any final adjustments.

- First Working example

## Keypoints

- intro, what is linear regression used for?
- plot data
- understand slope and y-intercept
- measure of goodness of fit
- gradient descent
- deriving the loss function
- little hint at alpha
- setep by step gradient descent
- python code for gradient descent
- hint into the future (optimizations)


## Script

### Series Introduction

Hello everyone to my first video on
this channel. This video is part of a series that aims to
teach the fundamentals of machine learning and progressivly
build up to more advanced topics. Such as Convolutional
Neural Networks and Recurrent Neural Networks, how to
optimize them and how to implement them in Python.

In my opinion it is important to understand at least some of
the math behind machine learning to have a better intuition
of why some things work and others don't. That's why we will
be looking at a lot of formula's and equations in this
series. And I encourage you to try to follow along even if
the math is a bit over your head. I'll try my best to
explain everything in a way that is easy to understand.


### Video Introduction

The topic of this video is Linear Regression. So let's get
started right away.

### What is Linear Regression?

The first question you might
have is what is Linear Regression? It is actually a very
simple concept. 

[Vis]

We have a set of data points, and we
want to find a line that fits the data points as good as
possible.

As an example: You want to forcast your companies revenue
for the next year based on the revenue of the last 10 years.

[Visualize line changes] In this case you would simply have
to fit a line to the data points, let's pick this one for
example and then plug next year into the line equation.

Which in this case would give us: 1.5 Million Dallars of
revenue.


### Line Equation

Let's start from the beginning. Our
desired result will be in the form of this equation. Where m
denotes the slope and b denotes the y-intercept of the line.

So if we change just b we simply move the line up and down.
And if we change just m we change it's slope.

### Measuring the goodness of fit

Now we have the general
equation of a line, so all we need to find is the best
values for m and b.

One approach to this is to try out a lot of different values
for m and b and then pick the best one.

But the question is how do we know which one is the best?
For that we need some measure of goodness of fit.

A simple version of this is to sum the distance of each data
point to the line. [Sum Error]

This seams to work okay, but it has a few problems:
1. If we just add more points this Error will become
astronomically large.
2. Two points that are on the opposite side of the line will
cancel out. [Show bad example]

Luckily both of them are easyly fixed.

First instead of just summing the error terms we can take
the average. Now our Error doesn't scale with the number of
data points anymore. [Mean Error] Second to stop points on
the opposite side from canceling out we can squere the error
terms before taking the average of them. [Mean Square Error]

Now that we have a measure for the well badness of a line.
We can randomly generate some lines and pick the one with
the lowest Error. And you can get pretty smart with this and
generate 10 lines and then pick the best 2 and generate 10
slightly different lines from those until you are satisfied
with the result. This is a kind of evolutionary algorithm
that we won't really cover in this series. Once we move on
to bigger problems it becomes harder to use this approach so
we will take a different route.

### Gradient Descent

Let's focus on a single line and see if
we can improve it. [Show bad line]

What's really important to understand now is that we want to
decrease the Error of the line, which itself is a function
of m, b and the data points. Let's simplify this a bit and
just look at the Error as a function of m and the data
points. So we ignore b for now. Here is a rough example of
how the Error function could look like. [Error Function
Visual]

Since we want the Error to be as small as possible we want
to find the minimum of this function. Which is located right
here.

In practice this function will typically be a lot more
complicated. so we can't just pinpoint the minimum.

For now let's just assume that we know the slope of the
Error function at any point. This is called the gradient or
the derivative of the function. We will calculate this in
the next step. For now let's just pretend that we already
know it.

Now we can simply take a random value for m and then move
into the direction that minimizes the Error. What I hope
becomes obvious now is that we can repeat this process over
and over again until we are satisfied with the result what
ever that may mean.

So now we optimized m but we still have to optimize b. This
a as simple as doing what we did for m but now be also do it
for b.

In this simple example if we give the computer enough time
it will eventually find the perfect values for m and b,
resulting in the line that best fits our data points.

We are almost done.

### Deriving the Loss Function In the last step we pretended
that we already know the derivative of the Error function.

So let's take a look at how we can actually calculate this.
I will not explain to you how to derive a function in this
video. If you know how to, that's great you can try it out
yourself before looking at my solution. If you don't know
how to do it, don't worry. It is not required to know how to
do it.

First we take the derivative of the Error function with
respect to m. And second we take the derivative of the Error
function with respect to b.

Note how the only difference between the two is that here we
multiply by x and here we multiply by 1, which obviously can
be left out because it is just the identity.

### Step by Step Gradient Descent Let's put it all together
and then implement it in Python to conclude the video.

1. Start with a random set value for m and b.
2. Calculate the derivative of the Error function with
respect to m and b.
3. Step into the direction that minimizes the Error for both
m and b.
4. Repeat step 2 and 3 until you are satisfied with the
result.

### Python code

1. Line Equation: f(x) = mx + b
2. Mean Square Error E(x) = 1/n * sum((f(x) - y)^2)
3. LossM(x) = 1/n * sum(2 * (f(x) - y) * x)
4. LossB(x) = 1/n * sum(2 * (f(x) - y))
5. update m and b with:
    - m = m - learning_rate * LossM(x)
    - b = b - learning_rate * LossB(x)
6. Implement the loop and plot the result.






















