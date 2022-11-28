#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked
 * list contains a cycle
 * @list: a singly-linked list
 *
 * Return: If there is no cycle - 0
 * If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *row, *col;

	if (list == NULL || list->next == NULL)
		return 0;

	row = list->next;
	col = list->next->next;

	while (row && col && col->next)
	{
		if (row == col)
			return (1);
		row = row->next;
		col = col->next->next;
	}
	return (0);
}
