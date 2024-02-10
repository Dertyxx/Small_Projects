#pragma once
#include "pch.h"
#include "CLparcours.h"
#include "CLpoint3D.h"

class CLparcours3D : public CLparcours {
public:
	CLparcours3D(int taille) : CLparcours(taille) {}
	void message() {
		cout << "Calcul d'un parcours de type 3D" << endl;
	}
};