#pragma once
#include "pch.h"
#include "CLpoint.h"
#include <cmath>

	class CLparcours {
	protected:
		int taille;
		int nbPoints = 0;
		CLpoint** points;
	public:
		CLparcours(int taille) : taille(taille), nbPoints(0) {
			points = new CLpoint*[taille];
		}
		~CLparcours() {
			delete[] points;
		}
		virtual void ajouterPoint(CLpoint* point) {
			if (nbPoints < taille) {
				points[nbPoints++] = point;
			}
			else cout << "Limite de points atteinte !" << endl;
		}
		virtual float calculDistance() {
			float distance = 0;
			for (int i = 0; i < taille - 1; i++) {
				float Xa = points[i]->getX();
				float Xb = points[i + 1]->getX();
				float Ya = points[i]->getY();
				float Yb = points[i + 1]->getY();
				float Za = points[i]->getZ();
				float Zb = points[i + 1]->getZ();

				float deltaX = Xb - Xa;
				float deltaY = Yb - Ya;
				float deltaZ = Zb - Za;

				distance += sqrt(pow(deltaX, 2) + pow(deltaY, 2)  + pow(deltaZ, 2));
			}
			return distance;
		}
		virtual void message() = 0;
	};