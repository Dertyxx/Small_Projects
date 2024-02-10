#pragma once
#include "pch.h"
#include "CLparcours.h"

class CLparcours2D : public CLparcours{
public:
	CLparcours2D(int taille) : CLparcours(taille) {};
	void message() {
		cout << "Calcul d'un parcours de type 2D" << endl;
	}
};