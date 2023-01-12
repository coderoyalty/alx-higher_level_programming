#include "lists.h"
/**
 * check_cycle - check for cycle in a linked list
 * @list: head of the linked list
 * Return: 0 or 1 indicating success or failure
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *next;

	current = list;
	if (current == NULL || current->next == NULL)
		return (0);

	next = current->next;
	while (current && next->next && next->next->next )
	{
		if (current == next)
			return (1);
		current = current->next;
		next = next->next->next;
	}
	return (0);
}
