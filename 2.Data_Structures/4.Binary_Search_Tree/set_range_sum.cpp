#include <cstdio>
#include "stdlib.h"
#include <iostream>
#include <iomanip>
#include <stack>
// Splay tree implementation
using std::stack;
// Vertex of a splay tree
struct Vertex {
  int key;
  // Sum of all the keys in the subtree - remember to update
  // it after each operation that changes the tree.
  long long sum;
  Vertex* left;
  Vertex* right;
  Vertex* parent;

  Vertex(int key, long long sum, Vertex* left, Vertex* right, Vertex* parent)
  : key(key), sum(sum), left(left), right(right), parent(parent) {}
};

Vertex* root = NULL;

/*void preorder(Vertex* node) {
  if (node == NULL)
    return;
  std::cout << node->key << " ";
  preorder(node->left);
  preorder(node->right);
}*/

void preorder(Vertex* p, int indent=0)
{
    if(p != NULL) {
        std::cout<< p->key << "\n ";
        if(p->left) preorder(p->left, indent+4);
        if(p->right) preorder(p->right, indent+4);
        if (indent) {
            std::cout << std::setw(indent) << ' ';
        }

    }
}

void update(Vertex* v) {
  if (v == NULL) return;
  v->sum = v->key + (v->left != NULL ? v->left->sum : 0ll) + (v->right != NULL ? v->right->sum : 0ll);
  if (v->left != NULL) {
    v->left->parent = v;
  }
  if (v->right != NULL) {
    v->right->parent = v;
  }
}

void small_rotation(Vertex* v) {
  Vertex* parent = v->parent;
  if (parent == NULL) {
    return;
  }
  Vertex* grandparent = v->parent->parent;
  if (parent->left == v) {
    Vertex* m = v->right;
    v->right = parent;
    parent->left = m;
  } else {
    Vertex* m = v->left;
    v->left = parent;
    parent->right = m;
  }
  update(parent);
  update(v);
  v->parent = grandparent;
  if (grandparent != NULL) {
    if (grandparent->left == parent) {
      grandparent->left = v;
    } else {
      grandparent->right = v;
    }
  }
}

void big_rotation(Vertex* v) {
  if (v->parent->left == v && v->parent->parent->left == v->parent) {
    // Zig-zig
    small_rotation(v->parent);
    small_rotation(v);
  } else if (v->parent->right == v && v->parent->parent->right == v->parent) {
    // Zig-zig
    small_rotation(v->parent);
    small_rotation(v);
  } else {
    // Zig-zag
    small_rotation(v);
    small_rotation(v);
  }
}

// Makes splay of the given vertex and makes
// it the new root.
void splay(Vertex*& root, Vertex* v) {
  if (v == NULL) return;
  while (v->parent != NULL) {
    //std::cout << "/* Splay loop */" << std::endl;
    if (v->parent->parent == NULL) {
      small_rotation(v);
      break;
    }
    big_rotation(v);
  }
  root = v;
}

// Searches for the given key in the tree with the given root
// and calls splay for the deepest visited node after that.
// If found, returns a pointer to the node with the given key.
// Otherwise, returns a pointer to the node with the smallest
// bigger key (next value in the order).
// If the key is bigger than all keys in the tree,
// returns NULL.
Vertex* search(Vertex*& root, int key) {
  Vertex* v = root;
  Vertex* last = root;
  Vertex* next = NULL;
  //std::cout << "/* Before search */" << std::endl;
  //preorder(root);
  //std::cout << std::endl;
  while (v != NULL) {
    //std::cout << "/* Search loop */  " << v->key << std::endl;
    if (v->key >= key && (next == NULL || v->key < next->key)) {
      next = v;
    }
    last = v;
    if (v->key == key) {
      break;
    }
    if (v->key < key) {
      v = v->right;
    } else {
      v = v->left;
    }
  }
  splay(root, last);
  //std::cout << "/* Searched */..." << (next==NULL?-1:next->key) << std::endl;
  //preorder(root);
  return next;
}

void split(Vertex* root, int key, Vertex*& left, Vertex*& right) {
  right = search(root, key);
  //std::cout << "right: " << (right==NULL?-1:right->key) << std::endl;
  splay(root, right);
  if (right == NULL) {
    left = root;
    return;
  }
  left = right->left;
  right->left = NULL;
  if (left != NULL) {
    left->parent = NULL;
  }
  update(left);
  update(right);
}

Vertex* merge(Vertex* left, Vertex* right) {
  if (left == NULL) return right;
  if (right == NULL) return left;
  Vertex* min_right = right;
  while (min_right->left != NULL) {
    min_right = min_right->left;
  }
  splay(right, min_right);
  right->left = left;
  update(right);
  return right;
}

// Code that uses splay tree to solve the problem

void insert(int x) {
  Vertex* left = NULL;
  Vertex* right = NULL;
  Vertex* new_vertex = NULL;
  split(root, x, left, right);
  if (right == NULL || right->key != x) {
    new_vertex = new Vertex(x, x, NULL, NULL, NULL);
  }
  root = merge(merge(left, new_vertex), right);
  //std::cout << "After insert: (k,l,r,p)" << new_vertex->key << new_vertex->left << new_vertex->right << new_vertex->parent << std::endl;
}

void erase(int x) {
  // Implement erase yourself
  Vertex* next = search(root,x+1);
  Vertex* v = search(root,x);
  //std::cout << "/* Erase */" << std::endl;
  if (next != NULL)
    splay(root,next);
  if (v != NULL)
    splay(root,v);

  if (v != NULL) {
    if (v->right == NULL) {
      if (v->parent != NULL) {
        if (v->parent->left == v) {
          v->parent->left = v->left;
          //std::cout << "/* message */" << std::endl;
        }
        else if(v->parent->right == v) {
          //std::cout << "/* message..1 */" << std::endl;
          v->parent->right = v->left;
        }
    }
    else {
        root = v->left;
    }

    if (v->left != NULL)
      v->left->parent = v->parent;
    free(v);
    //std::cout << "Root: " << root->key << std::endl;
    }
    else {
      //std::cout << "v->right=" << v->right->key << "v->left=" << v->left->key << "root:" << root->key << std::endl;
      //std::cout << "next->right=" << next->right << "root:" << root->key << std::endl;
      v->key = next->key;

      if (next->right != NULL)
        next->right->parent = next->parent;
      //std::cout << "/* message3 */" << std::endl;
      if (next->parent != NULL) {
        if (next->parent->left == next) {
          next->parent->left = next->right;
        }
        else if(next->parent->right == next) {
          next->parent->right = next->right;

        }
      }
      v->key = next->key;
      free(next);
    }
  }
}

bool find(int x) {
  // Implement find yourself
  //std::cout << "/* Find */" << std::endl;
  Vertex* v = search(root,x);
  if (v != NULL && v->key == x) {
    return true;
  }
  return false;
}

long long sum(int from, int to) {

  Vertex* left = NULL;
  Vertex* middle = NULL;
  Vertex* right = NULL;
  //std::cout << "Search 0 is: " << (a==NULL?-1:a->key) << std::endl;
  //std::cout << "Before split Root: " << (root==NULL?-1:root->key) << " root->left: " << (root->left==NULL?-1:root->left->key) << " root->right: " << (root->right==NULL?-1:root->right->key) << std::endl;
  //preorder(root);
  split(root, from, left, middle);
  split(middle, to + 1, middle, right);
  long long ans = 0;
  // Complete the implementation of sum
  //std::cout << ((left==NULL) ? -1:left->key) << " " << ((middle==NULL) ? -1:middle->key) << " " << ((right==NULL) ? -1:right->key) << std::endl;
  ans += ans + ((middle==NULL) ? 0:middle->sum);

  root = merge(merge(left,middle),right);
  //std::cout << "Root: " << (root==NULL?-1:root->key) << " root->left: " << (root->left==NULL?-1:root->left->key) << " root->right: " << (root->right==NULL?-1:root->right->key) << std::endl;
  //preorder(root);

  /*
  long long ans = 0;
  stack<Vertex*> temp;
  temp.push(root);
  while (!temp.empty()) {
    Vertex* p = temp.top();
    temp.pop();
    if (p->key >= from && p->key <= to) {
      ans += p->key;
    }
    if (p->right != NULL) {
      temp.push(p->right);
    }
    if (p->left != NULL) {
      temp.push(p->left);
    }
  }
  */
  return ans;
}

const int MODULO = 1000000001;

int main(){
  int n;
  scanf("%d", &n);
  int last_sum_result = 0;
  for (int i = 0; i < n; i++) {
    char buffer[10];
    scanf("%s", buffer);
    char type = buffer[0];
    switch (type) {
      case '+' : {
        int x;
        scanf("%d", &x);
        insert((x + last_sum_result) % MODULO);
      } break;
      case '-' : {
        int x;
        scanf("%d", &x);
        erase((x + last_sum_result) % MODULO);
      } break;
      case '?' : {
        int x;
        scanf("%d", &x);
        printf(find((x + last_sum_result) % MODULO) ? "Found\n" : "Not found\n");
      } break;
      case 's' : {
        int l, r;
        scanf("%d %d", &l, &r);
        long long res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO);
        printf("%lld\n", res);
        last_sum_result = int(res % MODULO);
      }
    }
  }
  return 0;
}
