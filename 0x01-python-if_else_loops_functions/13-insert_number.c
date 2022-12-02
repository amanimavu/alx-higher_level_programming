#include "lists.h"

/**
 * insert_node - inserts a node to an existing list
 * @head: first node of the list
 * @number: data of the node we are including
 *
 * Return: memory address of the inserted node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current, *before_current;

	if (!head || !*head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	before_current = *head;
	if (before_current->n >= number)
	{
		new->next = *head;
		return (new);
	}
	current = before_current->next;
	while (current)
	{
		if ((current->n) >= number)
		{
			new->next = current;
			before_current->next = new;
			break;
		}
		else
		{
			if (!current->next)
			{
				current->next = new;
				new->next = NULL;
			}
		}
		before_current = before_current->next;
		current = before_current->next;
	}
	return (new);
}
