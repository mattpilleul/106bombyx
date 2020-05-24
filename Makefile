##
## EPITECH PROJECT, 2019
## Project
## File description:
## Makefile
##

SRC	=	bombyx.py

NAME	=	106bombyx

all:	$(SRC)
	@cp $(SRC) $(NAME)
	@chmod 755 $(NAME)

clean:
	rm -f $(NAME)
	rm -f vgcore.*

fclean:	clean

re:	fclean all
