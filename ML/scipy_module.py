import scipy.stats as stats
def calculate_mean(data):
    return stats.tmean(data)

def calculate_mode(data):
    return stats
    mode_result = stats.mode(data)
    return mode_result.mode[0] if mode_result.count else None.mode(data)

def calculate_variance(data):
    return stats.tstd(data)**2

def calculate_standard_deviation(data):
    return stats.tstd(data)

def calculate_skewness(data):
    return stats.skew(data)

def calculate_kurtosis(data):
    return stats.kurtosis(data)

def calculate_correlation_coefficient(data1, data2):
    return stats.pearsonr(data1, data2)[0]

def calculate_covariance(data1, data2):
    return stats.pearsonr(data1, data2)[0] * stats.tstd(data1) * stats.tstd(data2)
def perform_t_test(data1, data2):
    t_stat, p_value = stats.ttest_ind(data1, data2)
    return t_stat, p_value
    return stats.mode(data)




# Run the demonstration
if __name__ == "__main__":
    print("Scipy Statistical Functions Demonstration")
    data1 = [10, 20, 20, 30, 40, 50]
    data2 = [15, 25, 35, 45, 55, 65]
    print("Data1:", data1)
    print("Data2:", data2)
    print("Mean of Data1:", calculate_mean(data1))
    print("Mode of Data1:", calculate_mode(data1))
    print("Variance of Data1:", calculate_variance(data1))
    print("Standard Deviation of Data1:", calculate_standard_deviation(data1))
    print("Skewness of Data1:", calculate_skewness(data1))
    print("Kurtosis of Data1:", calculate_kurtosis(data1))
    print("Correlation Coefficient between Data1 and Data2:", calculate_correlation_coefficient(data1, data2))
    print("Covariance between Data1 and Data2:", calculate_covariance(data1, data2))
    t_stat, p_value = perform_t_test(data1, data2)
    print("T-Test between Data1 and Data2: t-statistic =", t_stat, ", p-value =", p_value)
    print("Mode of Data1:", calculate_mode(data1))
    print("Mode of Data2:", calculate_mode(data2))
    print("Covariance between Data1 and Data2:", calculate_covariance(data1, data2))