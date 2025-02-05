#include <stdio.h>
#include <string.h>

void magical_function(char *password) {
    // Mot de passe pour accéder à la fonction magique
    const char correct_password[] = "open_sesame";
    if (strcmp(password, correct_password) == 0) {
        char flag[] = "shellmates{4cc3s$_Gr4nt3d_suCc3ssFullY}"; //REAL FLAG HERE 
        printf("The flag is: %s\n", flag);
    } else {
        printf("Access denied! Wrong password.\n");
    }
}

void normal_function() {
    printf("Nothing to see here.\n");
}

int main() {
    char password[50];

    printf("Welcome to the challenge!\n");
    normal_function();

    // Demander le mot de passe
    printf("Enter the password to access the magical function: ");
    scanf("%49s", password);  // Limite la saisie à 49 caractères pour éviter le débordement

    magical_function(password);
    return 0;
}