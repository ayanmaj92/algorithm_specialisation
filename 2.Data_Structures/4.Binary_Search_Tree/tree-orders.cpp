#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using std::vector;
using std::stack;
using std::ios_base;
using std::cin;
using std::cout;

void print(vector <int> a) {
  for (size_t i = 0; i < a.size(); i++) {
    if (i > 0) {
      cout << ' ';
    }
    cout << a[i];
  }
  cout << '\n';
}

class TreeOrders {
  int n;
  vector <int> key;
  vector <int> left;
  vector <int> right;

public:

  void read() {
    cin >> n;
    key.resize(n);
    left.resize(n);
    right.resize(n);
    for (int i = 0; i < n; i++) {
      cin >> key[i] >> left[i] >> right[i];
    }
  }

//Inorder implemented by iterative version, using a stack and
//a current pointer to the current node.
  vector <int> in_order() {
    vector<int> result;
    // Finish the implementation
    // You may need to add a new recursive method to do that
    //int i = 0;
    stack<int> temp;

    int current = 0;
    while (!temp.empty() || current != -1) {
      if (current != -1) {
        temp.push(current);
        current = left[current];
      }
      else {
        if (!temp.empty()) {
          result.push_back(key[temp.top()]);
          current = right[temp.top()];
          temp.pop();
        }
      }
    }

    return result;
  }
//Preorder implemented by iterative version using a stack.
  vector <int> pre_order() {
    vector<int> result;
    // Finish the implementation
    // You may need to add a new recursive method to do that
    stack<int> temp;
    temp.push(0);
    while (!temp.empty()) {
      int i = temp.top();
      temp.pop();
      result.push_back(key[i]);
      if (right[i] != -1) {
        temp.push(right[i]);
      }
      if (left[i] != -1) {
        temp.push(left[i]);
      }
    }
    return result;
  }
//Postorder implemented in iterative version using two stacks.
  vector <int> post_order() {
    vector<int> result;
    // Finish the implementation
    // You may need to add a new recursive method to do that
    stack<int> temp1,temp2;
    temp1.push(0);
    //int current = 0;
    while (!temp1.empty()) {
      /* code */
      int i = temp1.top();
      temp1.pop();
      temp2.push(i);
      if (left[i] != -1)
        temp1.push(left[i]);
      if (right[i] != -1)
        temp1.push(right[i]);
    }
    while (!temp2.empty()) {
      result.push_back(key[temp2.top()]);
      temp2.pop();
    }
    return result;
  }
};



int main() {
  ios_base::sync_with_stdio(0);
  TreeOrders t;
  t.read();
  print(t.in_order());
  print(t.pre_order());
  print(t.post_order());
  return 0;
}
