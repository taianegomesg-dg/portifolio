#include <iostream>
using namespace std;

int main() {
    // 1. Alocação dinâmica da variável MAX e leitura
    int* MAX = new int;
    cout << "Entre o MAX: ";
    cin >> *MAX;

    if (*MAX <= 0) {
        cout << "Por favor, insira um numero maior que zero." << endl;
        delete MAX; // Importante limpar a memória antes de sair!
        return 1;
    }

    // 2. Alocação dinâmica do vetor
    int* fib = new int[*MAX];

    // 3. Cálculo da sequência de Fibonacci
    if (*MAX > 0) fib[0] = 0;
    if (*MAX > 1) fib[1] = 1;

    for (int i = 2; i < *MAX; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    // 4. Impressão dos valores e endereços de memória
    for (int i = 0; i < *MAX; i++) {
        cout << fib[i] << " " << &fib[i] << endl;
    }

    // 5. Liberação da memória
    delete[] fib; 
    delete MAX;

    return 0;
}