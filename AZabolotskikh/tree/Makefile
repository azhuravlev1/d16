#
# Makefile for calc2 project, a simple lexer/parser with
#   a few extensions
#
# A. Thall
# CS 220 -- Spring 07
# 5. February 2007
#
# The makefile accomplishes the following build:
#
#   bison -y -d calc2.y
#   flex calc2.l
#   gcc -c y.tab.c lex.yy.c
#   gcc y.tab.o lex.yy.o -o calc2
#
# It also checks to see if symtab.h has been touched;
#   You can create an empty file or use it for your symbol-table

LEX = flex
CC = gcc -O2 -std=c99
YACC = yacc 

all:  y.tab.o lex.yy.o
	 $(CC) -o tree y.tab.o lex.yy.o

lex.yy.o:  lex.yy.c y.tab.h

y.tab.o: y.tab.c

y.tab.c y.tab.h:  tree.y
	$(YACC) -d tree.y

lex.yy.c:  tree.l
	$(LEX) tree.l

clean:
	rm -f lex.yy.o lex.yy.c y.tab.o y.tab.c y.tab.h tree
