#include <stdio.h>
#include <stdbool.h>

//Write a C Program to implement CPU scheduling algorithm. Display average waiting time and average TAT.

int main() {
	int n;
	printf("Enter number of process : ");
	scanf("%d",&n);
	
	int arrivalTime[n];
	int burstTime[n];
	int completionTime[n];
	int turnAroundTime[n];
	
	printf("Enter arrival time - \n");
	for(int i=0;i<n;i++){
		printf("\tfor event no.%d : ",i+1);
		scanf("%d",&arrivalTime[i]);
	}
	
	printf("Enter burst time - \n");
	for(int i=0;i<n;i++){
		printf("\tfor event no.%d : ",i+1);
		scanf("%d",&burstTime[i]);
	}

	int counter=0, currentTime=0, processCompleted=0;
	bool isBusy = false;
	
	while(processCompleted<n){
		
		if(counter>=burstTime[processCompleted]){
			isBusy = false;
			completionTime[processCompleted] = currentTime;
			processCompleted++;
			counter = 0;
		}
		if(arrivalTime[processCompleted]<=currentTime && !isBusy){
			isBusy = true;
		}
		if(isBusy){
			counter++;
		}
		
		currentTime++;
	}
	
	for(int i=0;i<n;i++){
		turnAroundTime[i] = completionTime[i]-arrivalTime[i];
	}
	
	printf("First Come First Serve [FCFS] : \n\tCompletion Time\t||\tTA Time\n");
	for(int i=0;i<n;i++){
		printf("\t%d \t\t\t\t||\t %d\n",completionTime[i],turnAroundTime[i]);
	}
	
	
//	for(int i=0;i<n;i++)
//		printf("%d",arrivalTime[i]);
	return 0;
}

/*
sample input
4
0 1 5 6
2 2 3 4

*/