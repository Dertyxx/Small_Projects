#include "pch.h"
#include "CESAR.h"
#include "XOR.h"

class CesarXor {
public:

	CESAR* CESARxor;
	XOR* cesarXOR;

	void encrypt(string& t_message, const int& t_keyCesar, const string& t_clexor, int t_option) {
		if (t_option == 1) {
			CESARxor->encrypt(t_message, t_keyCesar, t_option);
			cesarXOR->encrypt(t_message, t_clexor);
		}
		else {
			cesarXOR->encrypt(t_message, t_clexor);
			CESARxor->encrypt(t_message, t_keyCesar, t_option);
		}
	}
};