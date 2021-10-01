// Write a C program to implement grep command.

#include<stdio.h>
#include<string.h>
int main()
{
    char fn[10],pat[10],temp[200];
    FILE *fp;
    printf("Enter file name : ");
    scanf("%s",fn);
    printf("Enter pattern to be searched : ");
    scanf("%s",pat);
    fp=fopen(fn,"r");       //opening file in reading mode.
    printf("Result : \n");
    while(!feof(fp))        //checking weather it is the end of the file or not.
        {
            fgets(temp,1000,fp);        //fetching line from file
            if(strstr(temp,pat))
                printf("\t%s",temp);        // if condition satisfied then printing the line as result.
        }
    fclose(fp);         //closing file as work is done.
    return 0;
}