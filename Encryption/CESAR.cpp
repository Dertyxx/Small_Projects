#include "CESAR.h"


void CESAR::encrypt(string& t_message, int t_cle, int t_option) {

    for (char& letter : t_message) {
        if (isalpha(letter)) {
            char base = isupper(letter) ? 'A' : 'a';
            switch (t_option) {
            default:
                break;
            case 1:
                letter = ((letter - base + t_cle) % 26) + base;
                break;
            case 2:
                letter = ((letter - base - t_cle + 26) % 26) + base;
                break;
            }
        }
    }
    cout << "\n--------- Operation correctement effectuee ---------\n";
};

