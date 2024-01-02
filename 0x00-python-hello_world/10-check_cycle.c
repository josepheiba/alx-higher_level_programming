#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *ptr, *cnc;

	ptr = cnc = list;

	if (list == NULL)
		return (0);

	ptr = list;
	while (ptr != NULL && cnc != NULL && cnc->next != NULL)
	{
		ptr = ptr->next;
		cnc = cnc->next->next;

		if (ptr == cnc)
		{
			while (list != cnc)
			{
				list = list->next;
				cnc = cnc->next;
			}
			return (1);
		}
	}
	return (0);
}
