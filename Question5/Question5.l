
%{
#include<stdio.h>
int comment_byte=0;
int code_byte=0;
float comment_by_code;
%}




%%

\/\/(.*) {comment_byte += yyleng;};					

\/\*(.*\n)*.*\*\/  {comment_byte += yyleng;};

[{};,()]   {code_byte += yyleng;}						

[+-/=*%]   {code_byte += yyleng;}						

([a-zA-Z][0-9])+|[a-zA-Z]* {code_byte += yyleng;}

.|\n {code_byte += yyleng;}; 

<<EOF>>		{fprintf(yyout,"comment byte = %d \n",comment_byte);
			 fprintf(yyout,"code byte = %d \n",code_byte);
			 comment_by_code=(float)comment_byte/code_byte;
			 fprintf(yyout,"comment byte/code byte = %f \n",comment_by_code);
			 yyterminate();}	

%%


int yywrap()
{
return 1;
}



int main()
{
yyin=fopen("code.c","r");
yyout=fopen("out.c","w");

yylex();
return 0;
}
