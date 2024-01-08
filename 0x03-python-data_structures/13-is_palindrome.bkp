#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
        int l;
        int *int_array;
        l = 0;

        if (*head == NULL)
                return (1);

        find_tail(*head, &l);

        if (l == 1)
		return (1);

        int_array = malloc(sizeof(int) * l);

        fill_array(*head, &int_array);
        if (is_pad(int_array, (int_array + l)))
                return (1);
        return (0);
}

listint_t find_tail(listint_t *head, int *l)
{
        listint_t *new;
        new = head;
        while (new->next != NULL)
        {
                *l = *l + 1;
                new = new->next;
        }
        return (*new);
}

void fill_array(listint_t *head, int **int_array)
{
        listint_t *new;
        int i;

        new = head;
        i = 0;
        while (new != NULL)
        {
                (*int_array)[i] = new->n;
                new = new->next;
                i++;
        }
}

int is_pad(int *int_array, int *int_array_end)
{
       if (*int_array != *int_array_end)
       {
               return (0);
       }
       else if (int_array >= int_array_end)
               return (1);
       else
               return (is_pad(int_array + 1, int_array_end - 1));
}
