#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer to head
 * Return: 0 if it is not a palindrome, 1
 */
int is_palindrome(listint_t **head)
{
listint_t *current = *head, *palindrome = *head;
int count = 0, i = 0, j = 0;
if (!*head)
return (1);
while (current)
{
current = current->next;
count++;
}
current = *head;
for (i = 1; i <= count; i++)
{
for (j = i; j <= count - i; j++)
palindrome = palindrome->next;
if (current->n != palindrome->n)
return (0);
current = current->next;
palindrome = current;
}
return (1);
}
