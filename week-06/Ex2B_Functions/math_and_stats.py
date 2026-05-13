''' Lab 3 '''
import random
import math
import statistics

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

# calculations on vals_sample (subset of 75 values, integers 1-100)
sum75 = sum(vals_sample)
avg75 = statistics.mean(vals_sample)
median75 = statistics.median(vals_sample)
print(
    f"_Experimenting with a subset of integers 1-100:\n"
    f"Sum of 75 sample values from 1 to 100: {sum75}\n"
    f"Average of 75 sample values: {avg75:.2f}\n"
    f"Median of 75 sample values: {median75}"
)

# calculations on vals_choices (superset of 200 values, integers 1-100)
avg200 = statistics.mean(vals_choices)
median200 = statistics.median(vals_choices)
mode200 = statistics.mode(vals_choices)
stdev200 = statistics.stdev(vals_choices)
variance200 = statistics.variance(vals_choices)
print('\n')
print(
    f"_Experimenting with a superset of 200 values, integers 1-100:\n"
    f"Average of 200 values: {avg200:.2f}\n"
    f"Median of 200 values: {median200}\n"
    f"Mode of 200 values: {mode200}\n"
    f"Standard deviation of 200 values: {stdev200:.2f}\n"
    f"Variance of 200 values: {variance200:.2f}"
)

# calculating area of random circle
area_rounded_up = math.ceil(pi * (radius ** 2))
area_rounded_down = math.floor(pi * (radius ** 2))
print('\n')
print(
    f"_Modeling a random circle:\n"
    f"Radius = {radius}, area = {area_rounded_up} (rounded up to the nearest integer)\n"
    f"Radius = {radius}, area = {area_rounded_down} (rounded down to the nearest integer)"
)