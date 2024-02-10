#include "pch.h"

class GetChoices {
public:
	int action_choice;
	int methode_choice;
	GetChoices() {
		cout << "crypter (1) ou decrypter (2): ";
		cin >> action_choice;
		cout << "Methode Cesar (1) ou methode XOR (2) ou combinaison (3): ";
		cin >> methode_choice;
		cin.ignore(numeric_limits<streamsize>::max(), '\n');
	}
};