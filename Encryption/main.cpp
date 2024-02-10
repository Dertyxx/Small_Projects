
#include "pch.h"
#include "crypter.h"
#include "get_choices.h"
#include "input.h"
#include "savefile.h"


int main() {
	string message, cleXor;
	int cleCesar;

	GetChoices getchoices;
	Input input;
	Savefile savefile;
	XOR objXOR;
	CESAR objCESAR;
	CesarXor objCESARXOR;

	input.message_from_file(input.filename);
	input.input_key(getchoices.methode_choice);

	message = input.get_message();
	cleCesar = input.get_cleCesar();
	cleXor = input.get_cleXor();
	
	if (getchoices.methode_choice == 1) {
		objCESAR.encrypt(message, cleCesar, getchoices.action_choice);
	}
	else if (getchoices.methode_choice == 2) {
		objXOR.encrypt(message, cleXor);
	}

	else {
		objCESARXOR.encrypt(message, cleCesar, cleXor, getchoices.action_choice);
	}
	cout << message;
	
	savefile.save_to_file(savefile.new_filename, message);


}