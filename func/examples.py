import core_functions as cf

general_population = [i for i in range(100)]
test_sample = cf.simple_random_sample(general_population, 10)

# The average value of the sample
sample_mean = cf.mean(test_sample)
print(f"The average value of the sample: {sample_mean}\n")

# Sampling variance
sample_dispersion = cf.dispersion(test_sample)
print(f"Sample variance: {sample_dispersion}\n")

# Standard deviation of the sample
sample_standard_deviation = cf.standard_deviation(sample_dispersion)
print(f"Standard deviation of the sample: {sample_standard_deviation}\n")

z_elev = []
for i in test_sample:
    z_elev.append(round(cf.z_evaluation(i, sample_mean, sample_standard_deviation), 2))

print("All sample values with z-transformation: ", *z_elev)

