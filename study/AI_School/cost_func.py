

x = [2, 4, 8]
y = [5, 12, 21]

def cost_func(W, x, y):
    s = 0
    for i in range(len(x)):
        s += (W * x[i] - y[i]) ** 2

    return s / len(x)

print((cost_func(2, x, y)))


# for feed_W in range(-5, 6, 1):
#   curr_cost = cost_func(feed_W, x, y)
#   print("{:6.3f} | {:10.5f}".format(feed_W, curr_cost))