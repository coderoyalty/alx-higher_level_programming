#include "lists.h"
/**
 * check_cycle - check for cycle in a linked list
 * @list: head of the linked list
 * Return: 0 or 1 indicating success or failure
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;

	if (current == NULL)
		return (0);
	current = current->next;
	while (current)
	{
		if (current == list)
			return (1);
		current = current->next;
	}
	return (0);
}
