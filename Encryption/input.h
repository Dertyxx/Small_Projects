#include "pch.h"

class Input {
public:
	string message, cleXor, filename;
	int cleCesar;

	void message_from_file(string t_filename) {
		cout << "entrez le nom du fichier: ";
		cin >> t_filename;
		ifstream file(t_filename, ios::binary);
		if (file.is_open()) {
			ostringstream buffer;
			char character;
			while (file.get(character)) {
				buffer.put(character);
			}
			message = buffer.str();
			file.close();
		}
		else {
			std::cerr << "Erreur : Impossible d'ouvrir le fichier " << t_filename << std::endl;
		}
	};
	void input_key(int encryptType) {
		if (encryptType == 1) {
			cout << "Entrez la cle cesar (entier) : ";
			cin >> cleCesar;
		}
		else if (encryptType == 2) {
			cout << "Entrez la cle XOR (string):  ";
			cin >> cleXor;
		}
		else {
			cout << "Entrez la cle cesar (entier): ";
			cin >> cleCesar;
			cout << "Entrez la cle XOR (string): ";
			cin >> cleXor;
		}
	};
	string get_message() {
		return message;
	};
	int get_cleCesar() {
		return cleCesar;
	};

	string get_cleXor() {
		return cleXor;
	};
};