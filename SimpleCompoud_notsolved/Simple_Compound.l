%{
#include<stdio.h>
int flag=0;
%}




%%


(,?so |,?and |,?for |,?or |,?but |,?yet )(I |he |she |it |we |they |who |whom)		{printf("The Sentence is Compound \n");
											flag = 1;
																					 flag=1;}
<<EOF>>		{if(flag==0){printf("The Sentence is Simple \n");}
		else {
			printf(" ");}
			 yyterminate();}

			
%%


int yywrap()
{
return 1;
}

int main()
{
yyin=fopen("input.c","r");
yylex();
return 0;
}
