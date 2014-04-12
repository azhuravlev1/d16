//
//  main.c
//  SYA
//
//  Created by zaxdo on 12.04.14.
//  Copyright (c) 2014 zaxdo. All rights reserved.
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>



struct stack {
	int top;
	char conents[255];
};

int prec(char token) {
	switch (token) {
		case '+': return 1;
		case '-': return 2;
		case '*': return 3;
		case '/': return 4;
		case '^': return 5;
		case '(': return 0;
		default: abort();
	}
}

void push(struct stack *stack, char token){
	stack->conents[stack->top] = token;
	stack->top++;
}
char pop(struct stack *stack){
	char ret = stack->conents[stack->top-1];
	stack->top--;
	return ret;
}
char peek(struct stack *stack){
	return stack->conents[stack->top-1];
}

char *parse(char *expr, char *output) {
	int len = strlen(expr);
	struct stack stack;
	stack.top = 0;
	int outidx = 0;
	for (int i = 0; i<len; i++) {
		switch (expr[i]) {
			case '+':
			case '-':
			case '*':
			case '/':
			case '^':
				while (stack.top != 0) {
					if (prec(peek(&stack)) > prec(expr[i])) {
						output[outidx] = pop(&stack);
						outidx++;
					} else {
						break;
					}
				}
				push(&stack, expr[i]);
				break;
			case '(':
				push(&stack, '(');
				break;
			case ')':
				while (peek(&stack) != '(') {
					output[outidx] = pop(&stack);
					outidx++;
				}
				pop(&stack);
				break;
			case '\n':
				break;
			default:
				output[outidx] = expr[i];
				outidx++;
		}
	}
	while (stack.top != 0) {
		output[outidx] = pop(&stack);
		outidx++;
	}
	return output;
}

int main(int argc, const char * argv[]) {
	char number[10];
	fgets(number, 10, stdin);
	int tests;
	tests = atoi(number);
	char **exprs = malloc(sizeof(char*)*tests);

	for (int i = 0; i<tests; i++) {
		char expr[500];
		exprs[i] = malloc(sizeof(char*)*400);
		fgets(expr, 500, stdin);
		parse(expr, exprs[i]);
	}
	for (int i = 0; i<tests; i++) {
		puts(exprs[i]);
	}
    return 0;
}

