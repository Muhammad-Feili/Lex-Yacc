%{
#define SIZE 50         
#include<string.h>
#include <ctype.h>
char *strrev(char *str)
{
      char *p1, *p2;

      if (! str || ! *str)
            return str;
char *
strrev (char *str)
{
    if (!str) { 
        fprintf (stderr, "%s() Error: invalid string\n", __func__); 
        return NULL; 
    }

    char *begin = str;
    char *end = str + strlen (str) - 1;
    char tmp;

    while (end > begin)
    {
        tmp = *end;
        *end-- = *begin;
        *begin++ = tmp;
    }

    return str;
}      for (p1 = str, p2 = str + strlen(str) - 1; p2 > p1; ++p1, --p2)
      {
            *p1 ^= *p2;
            *p2 ^= *p1;
            *p1 ^= *p2;
      }
      return str;
}
char s[SIZE];
int top=-1;       

char infx[50],prfx[50],ch,elem;
char* INFX;
int i=0,k=0;
int j=0;
void push(char elem)
{                       /* Function for PUSH operation */
    s[++top]=elem;
}
 
char pop()
{                      /* Function for POP operation */
    return(s[top--]);
}
 
int pr(char elem)
{                 /* Function for precedence */
    switch(elem)
    {
    case '#': return 0;
    case ')': return 1;
    case '+':
    case '-': return 2;
    case '*':
    case '/': return 3;
    }
}
%}



%%

[()]     {infx[i] = *yytext;
	  i++;}
[0-9]+	 {infx[i] = atoi(yytext);
	  i++;}
[-+]	 {infx[i] = *yytext;
	  i++;}
[/*]	 {infx[i] = *yytext;
	  i++;}

<<EOF>>	    {
            push('#');
            strrev(infx);
            while( (ch=infx[i++]) != '\0')
            {
                if( ch == ')') push(ch);
                else
                    if(isalnum(ch)) prfx[k++]=ch;
                    else
                        if( ch == '(')
                        {
                            while( s[top] != ')')
                                prfx[k++]=pop();
                            elem=pop(); /* Remove ) */
                        }
                        else
                        {       /* Operator */
                            while( pr(s[top]) >= pr(ch) )
                                prfx[k++]=pop();
                            push(ch);
                        }
            }
            while( s[top] != '#')     /* Pop from stack till empty */
                prfx[k++]=pop();
            prfx[k]='\0';          /* Make prfx as valid string */
            strrev(prfx);
            strrev(infx);
            fprintf(yyout,"\n\nGiven Infix Expn: %s \n\n Prefix Expn: %s\n",infx,prfx);
	    yyterminate();            

}
    


%%

int main()
{         

    yyin=fopen("code.c","r");
    yyout=fopen("out.c","w");
    yylex();
    return 0;

    }
