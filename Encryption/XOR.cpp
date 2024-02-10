#include "XOR.h"

void XOR::encrypt(string& t_message, const string& t_cle) {
    int messageLength = t_message.length();
    int cleLength = t_cle.length();
    stringstream resultHex;
    for (int i = 0; i < messageLength; ++i) {
        char lettre = t_message[i];
        char cleCaractere = t_cle[i % cleLength]; 
        lettre ^= cleCaractere; 
        
        resultHex << lettre;
    }
    

    t_message = resultHex.str();
    cout << "\n--------- Operation correctement effectuee ---------\n";
}
    
 



