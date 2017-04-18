#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

class Node {
  public:
    int key;
    std::vector<Node*> children;
};

Node *root = NULL;

class TreeHeight {
  int n;
  std::vector<int> parent;

public:
  void read() {
    std::cin >> n;
    parent.resize(n);
    for (int i = 0; i < n; i++)
      std::cin >> parent[i];
    this->create_tree();
    //this->print_tree();
  }

  void create_tree() {
      Node* temp[parent.size()];
      //temp.resize(parent.size());
      for (int i = 0;i < parent.size(); i++)
        (temp[i]) = NULL;


      for (int i = 0; i < parent.size(); i++) {
        //std::cout << "Printing Temp" << std::endl;
        /*for (int j=0;j<parent.size();j++) {
          if(temp[j]!=NULL)
            std::cout << j<<":"<<temp[j]<<":"<<(temp[j])->key << " ";
        }*/
        if ((temp[i]) == NULL) {
          //std::cout << "Is NULL: " << i << "Parent[i]:" << parent[i] << std::endl;
          Node *node = new Node;
          //std::cout << "&node:"<<node << std::endl;
          (*node).key = i;
          temp[i] = node;

        }
        Node *node = (temp[i]);
        //std::cout << "Printing Temp" << std::endl;
        /*for (int j=0;j<parent.size();j++) {
          if(temp[j]!=NULL)
            std::cout << j<<":"<<temp[j]<<":"<<(temp[j])->key << " ";
        }*/
          if (parent[i] == -1) {
            //std::cout << "Root" << i << std::endl;
            root = temp[i];
            //std::cout << "Root is: " << *(temp[i])->key << std::endl;
            continue;
          }
          if ((temp[parent[i]]) == NULL) {
            //std::cout << "Parent Node NULL" << std::endl;
            Node *p = new Node;
            //std::cout << "&par:"<<p << std::endl;
            (*p).key = parent[i];
            //std::cout << "P.Key: "<< p.key << std::endl;
            temp[parent[i]] = p;

          }
          //std::cout << "Printing Temp" << std::endl;
          /*for (int j=0;j<parent.size();j++) {
            if(temp[j]!=NULL)
              std::cout << j<<":"<<temp[j]<<":"<<(temp[j])->key << " ";
          }*/
          //std::cout << "Add child" << std::endl;
          //std::cout << "Parent is:" << parent[i] << std::endl;
          Node *p = (temp[parent[i]]);
          (*p).children.push_back(node);

        }


  }

  void print_tree() {
    int height = 0;
    if (root == NULL) {
      std::cout << "/* message */" << std::endl;
      return;
    }
    std::queue<Node> Que;
    //std::cout << "Pushing Root: " <<  << std::endl;
    Que.push(*(root));
    height += 1;
    while (!Que.empty()) {
      Node n = Que.front();
      Que.pop();
      std::cout<<n.key<<"\t";
      if (!n.children.empty()) {
        height += 1;
        for (int i = 0; i<n.children.size(); i++) {

            Que.push(*(n.children[i]));
        }
      }
    }
    std::cout << "Height: " << height << std::endl;
  }

  int compute_height() {
    // Replace this code with a faster implementation
    /*
    int maxHeight = 0;
    for (int vertex = 0; vertex < n; vertex++) {
      int height = 0;
      for (int i = vertex; i != -1; i = parent[i])
        height++;
      maxHeight = std::max(maxHeight, height);
    }
    return maxHeight;
    */
    int height = 0;
    if (root == NULL) {
      //std::cout << "/* message */" << std::endl;
      return 0;
    }
    std::queue<Node> Que;
    //std::cout << "Pushing Root: " <<  << std::endl;
    Que.push(*(root));
    int num;
    while (1) {
      if (Que.empty()) {
        break;
      }
      height += 1;
      num = Que.size();
      while (num!=0) {
        Node n = Que.front();
        Que.pop();
        num -= 1;
        //std::cout<<n.key<<"\t";
        if (!n.children.empty()) {
          for (int i = 0; i<n.children.size(); i++) {
              Que.push(*(n.children[i]));
          }
        }
      }
  }
    return height;
  }
};

int main() {
  std::ios_base::sync_with_stdio(0);
  TreeHeight tree;
  tree.read();
  std::cout << tree.compute_height() << std::endl;
}
