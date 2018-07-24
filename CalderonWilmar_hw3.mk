CalderonWilmar_Resultados_hw3.pdf: CalderonWilmar_Plots_hw3.py
	python CalderonWilmar_Plots_hw3.py	
	pdflatex CalderonWilmar_Resultados_hw3.tex
	

CalderonWilmar_Plots_hw3.py: particula.txt frontfija.txt frontlib.txt
	./par.exe
	./tamb.exe

particula.txt: CalderonWilmar_ODE.cpp
	g++ CalderonWilmar_ODE.cpp -o par.exe

frontfija.txt frontlib.txt: CalderonWilmar_PDE.cpp
	g++ CalderonWilmar_PDE.cpp -o tamb.exe


