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
		return(node);
	}
	else
	{
		while(bold->next != NULL)
		{
			if(bold->next->n > number)
			{
				node->next = bold->next;
				bold->next = node;
				return (node);
			}
			bold = bold->next;
		}
		node->next = NULL;
		bold->next = node;
		return (node);
	}
	return (NULL);
}
