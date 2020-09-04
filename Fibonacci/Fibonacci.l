/* Lex Program to check whether a number is Fibonacci or Not */
  
%{ 
   /* Definition section */
   #include<stdio.h> 
   #include<stdlib.h> 
   int a,b,c,next,num; 
%} 
  

%% 
[0-9]+ {num=atoi(yytext); 
			 if((num==0)||(num==1))
			   printf("\n%d is a Fibonacci term",num);
			 else
			 {
			   a=0;
			   b=1;
			   c=a+b;
			   while(c<num)
			   {
			     a=b;
			     b=c;
			     c=a+b;
			   }
			   if(c==num)
			     printf("\n%d is a Fibonacci term",num);
			   else
			     printf("\n%d is not a Fibonacci term",num);
			 }
       } 
%% 
  
// driver code 
int main() 
 { 
  yylex(); 
  return 0; 
 } 