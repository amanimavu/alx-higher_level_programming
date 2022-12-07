#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if a sequence is a palindrome
 * @head: first node of the linked list
 *
 * Return: 1 if sequence is a palindrome or 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	int *int_array, i, size_of_array, lp_end_cond;

	i = 1;
	current = *head;
	while (current)
	{
		current = current->next;
		i += 1;
	}
	size_of_array = i - 1;
	int_array = malloc(sizeof(int) * size_of_array);
	if (!int_array)
	{
		printf("malloc failed");
		exit(EXIT_FAILURE);
	}
	current = *head;
	for (i = 0; i < size_of_array; i++)
	{
		int_array[i] = current->n;
		current = current->next;
	}
	if (size_of_array % 2)
		lp_end_cond = (size_of_array / 2) - 1;
	else
		lp_end_cond = (size_of_array / 2);

	for (i = 0; i <= lp_end_cond; i++)
	{
		if (int_array[i] != int_array[size_of_array - (i + 1)])
		{
			free(int_array);
			return (0);
		}
	}
	free(int_array);
	return (1);
}
