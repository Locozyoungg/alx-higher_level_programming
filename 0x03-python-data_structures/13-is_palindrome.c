#include <stddef.h>
#include "lists.h"

void reverse_list(listint_t **head);
int compare_lists(listint_t *list1, listint_t *list2);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return 1;

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *second_half = NULL;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    if (fast != NULL)
        slow = slow->next;

    reverse_list(&second_half);

    return compare_lists(*head, second_half);
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 */
void reverse_list(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

/**
 * compare_lists - compares two linked lists
 * @list1: first linked list
 * @list2: second linked list
 * Return: 1 if lists are the same, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
    while (list1 != NULL && list2 != NULL)
    {
        if (list1->n != list2->n)
            return 0;
        list1 = list1->next;
        list2 = list2->next;
    }

    return 1;
}
