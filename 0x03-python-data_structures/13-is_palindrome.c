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

	int_array = malloc(sizeof(int));
	if (!int_array)
	{
		printf("malloc failed");
		exit(EXIT_FAILURE);
	}

	i = 1;
	current = *head;
	while (current)
	{
		int_array[i - 1] = current->n;
		int_array = realloc(int_array, sizeof(int) * (i + 1));
		if (!int_array)
		{
			printf("realloc failed");
			exit(EXIT_FAILURE);
		}
		current = current->next;
		i += 1;
	}
	size_of_array = i - 1;
	if (size_of_array % 2)
		lp_end_cond = (size_of_array / 2) - 1;
	else
		lp_end_cond = (size_of_array / 2);

	for (i = 0; i <= lp_end_cond; i++)
	{
		if (int_array[i] != int_array[size_of_array - (i + 1)])
			return (0);
	}
	return (1);
}
