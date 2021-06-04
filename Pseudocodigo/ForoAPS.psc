Algoritmo ForoAPS
	Definir distFB, distFJ, distFA, distBA, distBJ, distAJ, suma Como Entero
	Definir  partida Como Caracter
	Escribir 'INGRESA LA DISTANCIA ENTRE:'
	Escribir 'F y B'
	Leer distFB
	Escribir 'F y J'
	Leer distFJ
	Escribir 'F y A'
	Leer distFA
	Escribir 'B y A'
	Leer distBA
	Escribir 'B y J'
	Leer distBJ
	Escribir 'A y J'
	Leer distAJ
	
	suma <- 0
	Escribir 'Indicar punto de partida:'
	Escribir '-> F / B / J / A :'
	Leer partida
	
	Si partida = 'F' Entonces
		Si distFB <= distFJ & distFB <= distFA & distBA <= distBJ Entonces
			suma <- distFB + distBA + distAJ + distFJ
			Escribir 'Ruta a seguir : F -> B -> A -> J -> F'
		SiNo
			Si distFA <= distFJ & distFA <= distFB & distBA <= distAJ Entonces
				suma <- distFA + distBA + distBJ + distFJ
				Escribir 'Ruta a seguir : F -> A -> B -> J -> F'
			SiNo
				Si distFJ <= distFB & distFJ <= distFA & distBJ <= distAJ Entonces
					suma <- distFJ + distBJ + distBA + distFA
					Escribir 'Ruta a seguir :   F -> J -> B -> A -> F'
				SiNo
					Si distFJ <= distFB & distFJ <= distFA & distAJ <= distBJ Entonces
						suma <- distFJ + distAJ + distBA + distFB
						Escribir 'Ruta a seguir : F -> J -> A -> B -> F'
					SiNo
						Si distFB <= distFJ & distFB <= distFA & distBJ <= distBA Entonces
							suma <- distFB + distBJ + distAJ + distFA
							Escribir 'Ruta a seguir : F -> B -> J -> A -> F'
						SiNo
							Si distFA <= distFJ & distFA <= distFB & distAJ <= distBA Entonces
								suma <- distFA + distAJ + distBJ + distFB
								Escribir 'Ruta a seguir : F -> A -> J -> B -> F'
							FinSi							
						FinSi						
					FinSi					
				FinSi				
			FinSi
		FinSi
	SiNo
		Si partida = 'B' Entonces
			Si distFB <= distBA & distFB <= distBJ & distFJ <= distFA Entonces
				suma <- distFB + distAJ + distBJ + distFB
				Escribir 'Ruta a seguir : B -> F -> J -> A -> B'
			SiNo
				Si distBJ <= distBA & distBJ <= distFB & distFJ <= distAJ Entonces
					suma <- distBJ + distFJ + distFA + distBA
					Escribir 'Ruta a seguir : B -> J -> F -> A -> B'
				SiNo
					Si distBA <= distFB & distBA <= distBJ & distAJ <= distFA Entonces
						suma <- distBA + distAJ + distFJ + distFB
						Escribir 'Ruta a seguir :   B -> A -> J -> F -> B'
					SiNo
						Si distBA <= distFB & distBA <= distBJ & distFA <= distAJ Entonces
							suma <- distBA + distFA + distFJ + distBJ
							Escribir 'Ruta a seguir : B -> A -> F -> J -> B'
						SiNo
							Si distBJ <= distBA & distBJ <= distFB & distAJ <= distFJ Entonces
								suma <- distBJ + distAJ + distFA + distFB
								Escribir 'Ruta a seguir : B -> J -> A -> F -> B'
							SiNo
								Si distFB <= distBA & distFB <= distBJ & distFA <= distFJ Entonces
									suma <- distFB + distFA + distAJ + distBJ
									Escribir 'Ruta a seguir : B -> F -> A -> J -> B'
								FinSi							
							FinSi						
						FinSi					
					FinSi				
				FinSi
			FinSi
		SiNo
			Si partida = 'J' Entonces
				Si distBJ <= distFJ & distBJ <= distAJ & distBA <= distFB Entonces
					suma <- distBJ + distBA + distFA + distFJ
					Escribir 'Ruta a seguir : J -> B -> A -> F -> J'
				SiNo
					Si distAJ <= distFJ & distAJ <= distBJ & distBA <= distFA Entonces
						suma <- distAJ + distBA + distFB + distFJ
						Escribir 'Ruta a seguir : J -> A -> B -> F -> J'
					SiNo
						Si distFJ <= distBJ & distFJ <= distAJ & distFB <= distFA Entonces
							suma <- distFJ + distFB + distBA + distAJ
							Escribir 'Ruta a seguir :   J -> F -> B -> A -> J'
						SiNo
							Si distFJ <= distBJ & distFJ <= distAJ & distFA <= distFB Entonces
								suma <- distFJ + distFA + distBA + distBJ
								Escribir 'Ruta a seguir : J -> F -> A -> B -> J'
							SiNo
								Si distBJ <= distFJ & distBJ <= distAJ & distFB <= distBA Entonces
									suma <- distBJ + distFB + distFA + distAJ
									Escribir 'Ruta a seguir : J -> B -> F -> A -> J'
								SiNo
									Si distAJ <= distFJ & distAJ <= distBJ & distFA <= distBA Entonces
										suma <- distAJ + distFA + distFB + distBJ
										Escribir 'Ruta a seguir : J -> A -> F -> B -> J'
									FinSi							
								FinSi						
							FinSi					
						FinSi				
					FinSi
				FinSi
			SiNo
				Si partida = 'A' Entonces
					Si distFA <= distBA & distFA <= distAJ & distFJ <= distFB Entonces
						suma <- distFA + distFJ + distBJ + distBA
						Escribir 'Ruta a seguir : A -> F -> J -> B -> A'
					SiNo
						Si distAJ <= distBA & distAJ <= distFA & distFJ <= distBJ Entonces
							suma <- distAJ + distFJ + distFB + distBA
							Escribir 'Ruta a seguir : A -> J -> F -> B -> A'
						SiNo
							Si distBA <= distFA & distBA <= distAJ & distFB <= distBJ Entonces
								suma <- distBA + distFB + distFJ + distAJ
								Escribir 'Ruta a seguir : A -> B -> F -> J -> A'
							SiNo
								Si distBA <= distFA & distBA <= distAJ & distBJ <= distFB Entonces
									suma <- distBA + distBJ + distFJ + distFA
									Escribir 'Ruta a seguir : A -> B -> J -> F -> A'
								SiNo
									Si distFA <= distBA & distFA <= distAJ & distFB <= distFJ Entonces
										suma <- distFA + distFB + distBJ + distAJ
										Escribir 'Ruta a seguir : A -> F -> B -> J -> A'
									SiNo
										Si distAJ <= distBA & distAJ <= distFA & distBJ <= distFJ Entonces
											suma <- distAJ + distBJ + distFB + distFA
											Escribir 'Ruta a seguir : A -> J -> B -> F -> A'
										FinSi							
									FinSi						
								FinSi					
							FinSi				
						FinSi
					FinSi			
				FinSi
			FinSi
		FinSi		
	FinSi
	Escribir 'Ruta optima ', suma, 'km' 
FinAlgoritmo