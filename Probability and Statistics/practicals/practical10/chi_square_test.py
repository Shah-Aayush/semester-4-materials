from scipy.stats import chi2


def chi_square_testing(observed_freq, expected_freq):
    chi_sq = 0
    for i in range(len(observed_freq)):
        chi_sq += ((observed_freq[i] - expected_freq[i]) ** 2) / expected_freq[i]
    return chi_sq


if __name__ == '__main__':
    observed = list(map(float, input("Enter observed frequency: \n").split()))
    expected = list(map(float, input("Enter expected frequency: \n").split()))
    level_of_significance = float(input("Enter level of significance: "))
    chi_square = chi_square_testing(observed, expected)
    critical_value = chi2.ppf(1 - level_of_significance, len(observed) - 1)
    print(chi_square)
    print(critical_value)
    if chi_square < critical_value:
        print("Accepted :)")
    else:
        print("Rejected :(")











"""
Enter observed frequency: 
35 30 15 15 5
Enter expected frequency: 
20 20 20 20 20
Enter level of significance: 0.05
30.0
9.487729036781154
Rejected
"""
