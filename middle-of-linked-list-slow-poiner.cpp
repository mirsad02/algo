// C++ program to illustrate how to find the middle element
// by using Floyd's Cycle Finding Algorithm
#include <iostream>
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

// Function to get the middle of the linked list
int getMiddle(Node* head) {
  
    // Initialize the slow and fast pointer to the head of
    // the linked list
    Node* slow_ptr = head;
    Node* fast_ptr = head;

    while (fast_ptr != NULL && fast_ptr->next != NULL) {

        // Move the fast pointer by two nodes
        fast_ptr = fast_ptr->next->next;

        // Move the slow pointer by one node
        slow_ptr = slow_ptr->next;
    }

    // Return the slow pointer which is currenlty pointing
    // to the middle node of the linked list
    return slow_ptr->data;
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

    cout << getMiddle(head) << endl;

    return 0;
}
