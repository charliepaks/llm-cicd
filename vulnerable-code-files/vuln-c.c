#include <stdio.h>
#include <string.h>

void vulnerable_function(char *input) {
    char buffer[10];
    strcpy(buffer, input); 
    printf("Input: %s\n", buffer);
}

int main() {
    char user_input[100];
    printf("Enter input: ");
    scanf("%s", user_input);
    vulnerable_function(user_input);
    return 0;
}