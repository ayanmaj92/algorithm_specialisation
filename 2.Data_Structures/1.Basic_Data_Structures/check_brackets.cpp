#include <iostream>
#include <stack>
#include <string>

struct Bracket {
    Bracket(int type, int position):
        type(type),
        position(position)
    {}

    bool Matchc(char c) {
        if (type == '[' && c == ']')
            return true;
        if (type == '{' && c == '}')
            return true;
        if (type == '(' && c == ')')
            return true;
        return false;
    }

    char type;
    int position;
    int pos;
};

int main() {
    std::string text;
    getline(std::cin, text);
    std::stack <Bracket> opening_brackets_stack;
    int flag = 0;
    int position;
    int pos;
    for (position = 0; position < text.length(); ++position) {
        char next = text[position];

        if (next == '(' || next == '[' || next == '{') {
            // Process opening bracket, write your code here
            opening_brackets_stack.push(Bracket(next,position));
        }

        if (next == ')' || next == ']' || next == '}') {
            // Process closing bracket, write your code here
            if (opening_brackets_stack.empty()) {
              flag = 1;
              break;
            }
            Bracket top_char = opening_brackets_stack.top();

            if (!top_char.Matchc(next))
            {
              flag = 1;
              //pos = position + 1;
              break;
            }
            else {
                opening_brackets_stack.pop();
            }
        }
    }

    // Printing answer, write your code here
    //Correct logic here
    if (!opening_brackets_stack.empty() && flag == 0) {
      //It means we have inputted only opening brackets!
      std::cout <<opening_brackets_stack.top().position+1;
    }
    else if (flag == 1) {
      /* code */
      //It means that we have had a mismatch and there has been at least
      //one matching closing bracket or the stack went empty before we get a
      //closing bracket
      //Flag 1 means a bracket is mismatched, either by type of bracket
      //or because there are no opening brackets to balance.
      std::cout << ++position;
    }
    else
      std::cout << "Success";
    return 0;
}
