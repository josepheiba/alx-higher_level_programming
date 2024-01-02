#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *bold = *head;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	
	node->n = number;
	node->next = NULL;

	if (*head == NULL)
	{
		*head = node;
		return(new);
	}
	else
	{
		while(bold->next != NULL)
		{
			if(bold->next->n > number)
			{
				bold->next = bold->next;
				bold->next = new;
				return (new);
			}
			bold = bold->next;
		}
		bold->next = NULL;
		bold->next = new;
		return (new);
	}
	return (NULL);
}
