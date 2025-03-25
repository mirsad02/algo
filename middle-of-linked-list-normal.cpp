// C++ program to illustrate how to find the middle element
// by counting the number of nodes
#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int data;
    Node* next;
  
    Node(int x) {
        this->data = x;
        this->next = nullptr;
    }
};

// Helper function to find length of linked list
int getLength(Node* head) {

    // Variable to store length
    int length = 0;

    // Traverse the entire linked list and increment length by
    // 1 for each node
    while (head) {
        length++;
        head = head->next;
    }

    // Return the number of nodes in the linked list
    return length;
}

// Function to find the middle element of the linked list
int getMiddle(Node* head) {

    // Finding length of the linked list
    int length = getLength(head);

    // traverse till we reached half of length
    int mid_index = length / 2;
    while (mid_index--) {
        head = head->next;
    }

    // Head now will be pointing to the middle element
    return head->data;
}

int main() {

    // Create a hard-coded linked list:
    // 10 -> 20 -> 30 -> 40 -> 50 -> 60 
    Node* head = new Node(10);
    head->next = new Node(20);
    head->next->next = new Node(30);
    head->next->next->next = new Node(40);
    head->next->next->next->next = new Node(50);
    head->next->next->next->next->next = new Node(60);

    cout << getMiddle(head);

    return 0;
}
