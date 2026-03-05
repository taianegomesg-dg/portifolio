#include <iostream>

using namespace std;

int main() {
    int n1, n2, soma;

    cout << "--- CALCULADORA DE SOMA ---" << endl;
    cout << "Digite o primeiro numero: ";
    cin >> n1; // Aqui o programa para e espera você digitar

    cout << "Digite o segundo numero: ";
    cin >> n2;

    soma = n1 + n2;

    cout << "A soma de " << n1 << " com " << n2 << " e igual a: " << soma << endl;

    return 0;
}