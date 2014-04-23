%{
#include <stdio.h>
#include "y.tab.h"
%}

%%
[0-9]+			yylval.ival=atoi(yytext);return NUMBER;
[a-zA-Z][a-zA-Z0-9]*	yylval.sval = strdup(yytext); return WORD;
\:						return COLON;
\,						return COMMA;
\(			return OPAREN;
\)			return CPAREN;
\n			;
[ \t]+			;
%%