#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *ptr, *cnc;

	ptr = cnc = list;

	if (list == NULL)
		return (0);

	while (ptr != NULL && cnc != NULL && cnc->next != NULL)
	{
		ptr = ptr->next;
		cnc = cnc->next->next;

		if (ptr == cnc)
		{
			return (1);
		}
	}
	return (0);
}
