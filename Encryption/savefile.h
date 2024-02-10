#include "pch.h"

class Savefile {
public: 
    string new_filename;
    void save_to_file( string& t_newfilename, const string& t_message) {
        cout << "entrez le nom du fichier de sauvegarde: ";
        cin >> t_newfilename;
        ofstream file(t_newfilename, ios::binary);

        if (file.is_open()) {
            file .write(t_message.c_str(), t_message.size());
            file.close();
            cout << "Message enregistre avec succes dans le fichier " << t_newfilename << std::endl;
        }
        else {
            cerr << "Erreur : Impossible d'ouvrir le fichier " << t_newfilename << std::endl;
        }
    }
};