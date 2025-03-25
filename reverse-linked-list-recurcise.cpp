// Recursive C++ program to reverse a linked list

#include <bits/stdc++.h>
using namespace std;

class Node {
  public:
    int data;
    Node *next;

    Node(int new_data) {
        data = new_data;
        next = nullptr;
    }
};

// Given the head of a list, reverse the list
// and return the head of reversed list
Node *reverseList(Node *head) {
    if (head == NULL || head->next == NULL)
        return head;

    // reverse the rest of linked list and put
    //  the first element at the end
    Node *rest = reverseList(head->next);

    // Make the current head as last node of
    // remaining linked list
    head->next->next = head;

    // Update next of current head to NULL
    head->next = NULL;

    // Return the reversed linked list
    return rest;
}

void printList(Node *node) {
    while (node != nullptr) {
        cout << " " << node->data;
        node = node->next;
    }
}

int main() {

    // Create a hard-coded linked list:
    // 1 -> 2 -> 3 -> 4 -> 5
    Node *head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);
    head->next->next->next = new Node(4);
    head->next->next->next->next = new Node(5);

    cout << "Given Linked List:";
    printList(head);

    head = reverseList(head);

    cout << "\nReversed Linked List:";
    printList(head);

    return 0;
}

