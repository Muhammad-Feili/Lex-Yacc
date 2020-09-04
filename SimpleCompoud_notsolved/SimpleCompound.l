%{ 
#include<stdio.h> 
#include<string.h> 
int i = 0; 
int j;
char words[100];
%} 
  

%% 
[a-zA-Z]+	{ words[i]=yytext;
					i++;} 
  
\n	{ 
  	for (j=0;j<i;j++){
  		printf("words:: %s", words[j]);
  	    }
	for(j=0;j<i;j++){
		words[j]=' ';
	}
	i=0;
      } 
%% 
  
int yywrap(void){} 
  
int main() 
{    
    
    yylex();
    return 0; 
} 
