int is_palindrome(listint_t **head)
{
        find_tail(**head);
}

listint_t find_tail(listint_t **head)
{
        while (head->next != NULL)
        {
                head = head->next;
        }
        return (**head);
}
