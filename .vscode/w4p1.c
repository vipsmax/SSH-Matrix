/*
*****************************************************************************
                          Workshop - #4 (P1)
Full Name  : 
Student ID#: 
Email      : 
Section    : 
Authenticity Declaration:
I declare this submission is the result of my own work and has not been
shared with any other student or 3rd party content provider. This submitted
piece of work is entirely of my own creation.
*****************************************************************************
*/

#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <conio.h>
#include<stdlib.h>

int main(void)
{

    char loop;
    int itr,i=1;
    clrscr();
    printf("D = do/while | W = while | F = for | Q = quit\n");
    printf("Enter loop type and the number of times to iterate (Quit=Q0):");
    scanf("%c%d",&loop,&itr);
    if(loop=='D')
    {
	if(itr>3)
	{
	    printf("DO-WHILE:-");
	    do
	    {
		printf("D");
		i=i+1;
	    }while(i<=itr);
	}else
	{
	    printf("ERROR: The number of iterations must be between 3-20 inclusive!");
	}

    }else if(loop=='W')
    {
	if(itr>3)
	{
	    printf("WHILE:-");
	    while(i<=itr)
	    {
		printf("W");
		i=i+1;
	    }
	}else
	{
	    printf("ERROR: The number of iterations must be between 3-20 inclusive!");
	}

    }else if(loop=='F')
    {
	if(itr>3)
	{
	    printf("FOR:-");
	    for (i=1; i <= itr; i++)
	    {
		printf("F");
	    }

	}else
	{
	    printf("ERROR: The number of iterations must be between 3-20 inclusive!");
	}


    }else if (loop=='Q')
     {
	    exit(0);
     }else
     {
	 printf("ERROR: Invalid entered value(s)!");
     }


   // return 0;
    getch();
}
