%{
#include <stdio.h>
#include <stdlib.h>
struct stack {
	int top;
	void *conents[255];
};
struct tree {
	char *word;
	int distance;
	int numLeaves;
	struct tree **leaves;
};
void pushTree(char*,int);
void popTreeAndAttachToParent();
void yyerror(char*);
#ifdef DEBUG
#define LOG(s) fprintf(stderr, "%s:%s\n",__PRETTY_FUNCTION__, s)
#else
#define LOG(s)
#endif
%}

%token COLON COMMA OPAREN CPAREN NEXT;
%union {
	int ival;
	char *sval;
}
%token <ival> NUMBER
%token <sval> WORD

%%
tree:
	OPAREN WORD COLON NUMBER COLON {pushTree($2, $4);} subtrees CPAREN {popTreeAndAttachToParent();};

subtrees:/*empty*/| tree | tree COMMA subtrees;
%%
extern int yylex();
extern int yyparse();
extern FILE *yyin;
struct stack stack;
struct tree *ret;

#define TYPE struct tree*
static void push(struct stack *stack, TYPE item){
	stack->conents[stack->top] = item;
	stack->top++;
}
static TYPE pop(struct stack *stack){
	TYPE ret = stack->conents[stack->top-1];
	stack->top--;
	return ret;
}
static TYPE peek(struct stack *stack){
	return stack->conents[stack->top-1];
}
#undef TYPE

void pushTree(char *word, int dist) {
    LOG("STARTD");
	#ifdef DEBUG
    printf("%s%d\n", word,dist);
	#endif
    struct tree *tree;
    tree = calloc(1,sizeof(struct tree));
    tree->word = word;
    tree->distance = dist;
    push(&stack, tree);
}
void popTreeAndAttachToParent(){
	LOG("FINISHD");
	struct tree *newTree = pop(&stack);
	if (stack.top==0) {
		ret = newTree;
		return;
	}
	struct tree *parent = peek(&stack);
	parent->leaves = realloc(parent->leaves, (parent->numLeaves+1)*sizeof(struct tree*));
	parent->leaves[parent->numLeaves] = newTree;
	parent->numLeaves++;
}
void printTree(struct tree *tree){
    printf("(%s::%d::", tree->word,tree->distance);
    for (int i = 0;i<tree->numLeaves;i++){
	printTree(tree->leaves[i]);
    }
    printf(")");
}


int main(int argc, const char **argv) {
	LOG("BEGIN");
	if (!(yyin = fopen("a.snazzle", "r"))) {
		puts("ioerror");
		return -1;
	}
	LOG("OPEND");
	stack.top = 0;
	do {
		yyparse();
	} while (!feof(yyin));
	LOG("PARSD");
	printTree(ret);
	
}

void yyerror(char *s) {
	LOG("ERRORD");
	puts(s);
	exit(-1);
}
int yywrap() {return 1;}
