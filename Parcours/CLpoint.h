#pragma once
#include "pch.h"

	class CLpoint {
	protected:
		float x, y, z;
		static int quantity;
	public:
		CLpoint(float x, float y) : x(x), y(y) {
			this->quantity++;
		}
		virtual void afficherCoordo() const {
			cout << "\nles coordonndes du point 2D : " << this << ", d'ID : " << quantity <<endl;
		}
		virtual float getX() { return this->x; }
		virtual float getY() { return this->y; }
		virtual float getZ() { return this->z; }
	};