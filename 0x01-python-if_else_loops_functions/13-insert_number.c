#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - function inserts a number into a sorted singly linked list.
 * @head: head of linked list
 * @number: number to insert
 * Return: the address of the new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new, *current;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
new->next = NULL;
if (*head == NULL || number < (*head)->n)
{
new->next = *head;
*head = new;
}
else
{
current = *head;
while (current->next != NULL &&
current->next->n < number)
{
current = current->next;
}
new->next = current->next;
current->next = new;
}
return (new);
}
