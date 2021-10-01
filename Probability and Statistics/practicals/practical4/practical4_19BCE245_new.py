# Write a program which reads 500 real values and computes and displays their (i) mean (ii) variance (iii) standard deviation. The program should also output z-score for each value. The program should furthermore display (i) scatter plot (ii) histograms for these numbers for n bins where n is read from the user and (iii) density plot assuming Gaussian as the probability density function.

import math
import matplotlib.pyplot as plt

def gaussFunction(s, x, m):
    return (1 / (s * math.sqrt(2 * math.pi))) * math.exp((-1 / 2) * math.pow((x - m) / s, 2))

if __name__ == "__main__":
    arr1 = []		#for storing 1st list
    arr2 = []		#for storing 2nd list
    
    total_size = int(input("Enter the size of the array : "))
    size = int(total_size/2)
    
    temp_number = float()
    
    print("Enter first",size,"elements for array 1 : ")
    for i in range(size):
        temp_number = float(input("\tEnter element no.{} : ".format(i+1)))
        arr1.append(temp_number)
    
    #calculating sum of all elements and mean
    sum_of_arr1 = sum(arr1)
    mean_of_arr1 = float(sum_of_arr1/size)
    print("For arr1, Sum is",sum_of_arr1,"and Mean is",mean_of_arr1)
    
    print("Enter last",size,"elements for array 2 : ")
    for i in range(size):
        temp_number = float(input("\tEnter element no.{} : ".format(size + i + 1)))
        arr2.append(temp_number)
        
    sum_of_arr2 = sum(arr2)
    mean_of_arr2 = float(sum_of_arr2/size)
    print("For arr2, Sum is",sum_of_arr2,"and Mean is",mean_of_arr2)
    
    #calculating variance and SD
    arr1_diff = []
    arr2_diff = []
    sq_sum_of_arr1 = 0
    sq_sum_of_arr2 = 0
    
    for i in range(size):
        arr1_diff.append(float(arr1[i]-mean_of_arr1))
        sq_sum_of_arr1 += float(arr1_diff[i]**2)
        
    variance1 = float(sq_sum_of_arr1/size)
    sd1 = math.sqrt(variance1)
    print("For arr1, Variance is",variance1)
    print("For arr1, SD is",round(sd1,2))
    
    for i in range(size):
        arr2_diff.append(float(arr2[i]-mean_of_arr2))
        sq_sum_of_arr2 += float(arr2_diff[i]**2)
        
    variance2 = float(sq_sum_of_arr2/size)
    sd2 = math.sqrt(variance2)
    print("For arr2, Variance is",variance2)
    print("For arr2, SD is",round(sd2,2))
    
    z = []      #for storing z scores
    
    #calculating z-score 
    for i in range(size):
        z.insert(i, (arr1[i] - mean_of_arr1) / sd1)
        z.insert(i, (arr2[i] - mean_of_arr2) / sd1)
    
    print("For array1 : ")
    print("VALUE\t\tZ-SCORE")
    for index in range(size):
        print(arr1[index],"\t\t",round(z[index],2))
        
    print("For array2 : ")
    print("VALUE\t\tZ-SCORE")
    for index in range(size):
        print(arr1[index],"\t\t",round(z[size + index],2))
        
    arr1.sort()
    arr2.sort()
    
    g1, g2 = [], []
    for i in range(size):
        g1.append(gaussFunction(sd1, arr1[i], mean_of_arr1))
        g2.append(gaussFunction(sd2, arr2[i], mean_of_arr2))
        
    #Displaying histogram
    b = int(input("Enter number of bins for histogram : "))
    plt.subplot(2, 2, 1)
    plt.title("HISTOGRAM")
    arr = arr1 + arr2
    plt.hist(arr,bins=b, color='r')
    
    #Displaying scatterplot
    plt.subplot(2, 2, 2)
    plt.title("SCATTERPLOT")
    plt.scatter(arr[:total_size // 2], arr[total_size // 2:] )
    
    #displaying gaussian fx. for first half of the array
    plt.subplot(2, 2, 3)
    plt.title("GAUSSSIAN FUNCTION 1")
    plt.plot(arr1, g1, color='y')
    
    #displaying gaussian fx. for second half of the array
    plt.subplot(2, 2, 4)
    plt.title("GAUSSSIAN FUNCTION 2")
    plt.plot(arr2, g2, color='g')
    
    plt.tight_layout()		#improves subplot spacings 
    plt.show()