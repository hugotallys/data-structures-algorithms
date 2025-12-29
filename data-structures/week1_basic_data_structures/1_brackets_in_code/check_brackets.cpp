#include <iostream>
#include <ostream>
#include <stack>
#include <string>

struct Bracket {
    char type;
    int position;

    Bracket(char type, int position) {
        this->type = type;
        this->position = position;
    }

    bool Matchc(char c) {
        if (type == '[' && c == ']')
            return true;
        if (type == '{' && c == '}')
            return true;
        if (type == '(' && c == ')')
            return true;
        return false;
    }
};

int main() {
    std::string text;
    getline(std::cin, text);

    std::stack <Bracket> opening_brackets_stack;
    for (int position = 0; position < text.length(); ++position) {
        char next = text[position];

        if (next == '(' || next == '[' || next == '{') {
            Bracket current{next, position};
            opening_brackets_stack.push(current);
        }

        if (next == ')' || next == ']' || next == '}') {
            if (!opening_brackets_stack.empty()) {
                Bracket top = opening_brackets_stack.top();
                if (top.Matchc(next)) {
                    opening_brackets_stack.pop();
                } else {
                    Bracket current{next, position};
                    opening_brackets_stack.push(current);
                    break;
                }
            } else {
                Bracket current{next, position};
                opening_brackets_stack.push(current);
                break;
            }
        }
    }

    if (opening_brackets_stack.empty()) {
        std::cout << "Success" << std::endl;
    } else {
        Bracket top = opening_brackets_stack.top();
        std::cout << top.position + 1 << std::endl;
    }

    return 0;
}
