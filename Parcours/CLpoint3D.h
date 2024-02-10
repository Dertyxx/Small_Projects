#pragma once
#include "pch.h"
#include "CLpoint.h"

	class CLpoint3D :public CLpoint{
	public:
		CLpoint3D(float x, float y, float z) : CLpoint(x, y) {
			this->z = z;
			this->quantity++;
		}
		void afficherCoordo() const {
			cout << "les coordonndes du point 3D : " << this << ", d'ID : " << quantity<< endl ;
		}
	
	};