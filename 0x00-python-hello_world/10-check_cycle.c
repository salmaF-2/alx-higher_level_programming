#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - function to Checks if a singly linked list has a cycle in it
 * @list: Pointer to the head of linked list.
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
listint_t *mvnode, *mvtwonode;
if (list == NULL || list->next == NULL)
return (0);
mvnode = list;
mvtwonode = list->next;
while (mvnode != mvtwonode)
{
if (mvtwonode == NULL || mvtwonode->next == NULL)
return (0);
mvnode = mvnode->next;
mvtwonode = mvtwonode->next->next;
}
return (1);
}
