#include "lists.h"
/**
 * check_cycle - checks if the list cyles or
 * ends with a null pointer
 * @list: a single linked list
 *
 * Return: 1 if the list has a cyles 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *current;

	current = list;
	while (current)
	{
		current = current->next;
		if (current == list)
			return (1);
	}
	return (0);
}
