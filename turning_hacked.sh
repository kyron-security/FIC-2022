#/bin/sh
while true ; do
	python hackit.py "HACKED    " "  HACKED  " "    HACKED"
	python hackit.py "ACKED     " " HACKED   " "   HACKED "
	python hackit.py "CKED      " "HACKED    " "  HACKED  "
	python hackit.py "KED       " "ACKED     " " HACKED   "
	python hackit.py "ED        " "CKED      " "HACKED    "
	python hackit.py "D         " "KED       " "ACKED     "
	python hackit.py "          " "ED        " "CKED      "
	python hackit.py "         H" "D         " "KED       "
	python hackit.py "        HA" "          " "ED        "
	python hackit.py "       HAC" "         H" "D         "
	python hackit.py "      HACK" "        HA" "          "
	python hackit.py "     HACKE" "       HAC" "         H"
	python hackit.py "    HACKED" "      HACK" "        HA"
	python hackit.py "   HACKED " "     HACKE" "       HAC"
	python hackit.py "  HACKED  " "    HACKED" "      HACK"
	python hackit.py " HACKED   " "   HACKED " "     HACKE"
	python hackit.py "HACKED    " "  HACKED  " "    HACKED"
done
