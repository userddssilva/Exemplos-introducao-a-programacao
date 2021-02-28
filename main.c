#include <stdio.h>
#include <stdlib.h>
#define TAM 20

void imprimir_vetor(int v[TAM]){
	int i;
	for (i = 0; i<TAM; i++){
		
		printf("%5d", v[i]);
	}
	printf("\n");
}
	
void ordenar_vetor(int v[TAM]){
	int i;
	int j;
	int aux;
	for(i = 0; i < TAM; i++){
		for(j = i+1; j<TAM-1; j++){
			if (v[i] > v[j]){
				aux = v[i];
				v[i] = v[j];
				v[j] = aux;
			
			}
		}	
	}
}


void copia_vetor(int va[TAM], int vb[TAM]) {
	int i;
	for(i = 0; i<TAM; i++){
		vb[i] = va[i];
	}
}

int main() {
	
	int copia_numeros[TAM];
	int i, j, aux, contador;
	
	int numeros[TAM] = {1, 0, 4, 3, -78, -45, -33, 5, 12, 90, 234, -2, 2, 33, 56, 11, 25, 90, 100, 543};
	
	copia_vetor(numeros, copia_numeros);
	
	printf("Vetor original antes da ordenacao\n");
	imprimir_vetor(numeros);
	
	ordenar_vetor(numeros);
	
	printf("Vetor original depois da ordenacao\n");
	imprimir_vetor(numeros);
	
	printf("Vetor copia original\n");
	imprimir_vetor(copia_numeros);
	
//	for(i = 0; i<TAM; i++){
//		
//		printf("%3d", copia_numeros[i]);
//	}
//	
	
	return 0;
}

