CREATION D'UNE APP DE COMPTABILITE MANIFESTANT LA PARTIE DOUBLE ET LES AUTRES PRINCIPES COMPTABLE

**STRUCTURATION DU DU DOSSIER APP**

-DATA: contient la base de donnee sqlite et est reserve a la conservation, gestion et stockage de donnee. Il sera composee d'une table bilan, compte de resultat, d'un espace journal, d'un grand livre et d'une balance si possible. Pour enregistrer une operation il faudra passer par un journal qui permetra de definir ensuite les autre documents comptables obligatoires tels que le grand livre et la balance, et ensuite definir les documents de synthese que sont le bilan et le compte de resutat.

Il ne contiendra que la base de donnes et ses tables

-MAIN: qui contiendra l'interface utilisateur le tkinter ou customtkinter. Il servira a de point de convergence du fichier metier et du fichier data

-METIER: contient les instructions et les differents calculs et regles de comptabilite. Il se servira des donnees du fichier DATA, afin de determiner les operations et faire les calcues et verifications necessaires quand il s'agira de la partie double. Il est des lors le cerveau de l'application, et jouera le role de
