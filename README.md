# Best Hacking League
## Zespół: Górnicy Carla Friedricha
### Kategoria: AI

![Hack Logo](/docs/img/logo.png)

Repozytorium zawiera rozwiązania przygotowane przez zespół w składzie:
* Jakub Dworzański, 
* Łukasz Łaszczuk, 
* Anna Szymanek,
* Patryk Wielopolski.

# Spis treści
1. [Cel](#cel)
2. [Dane](#dane)
3. [Rozwiązanie](#rozwiazanie)
    1. [Modele](#modele)
    2. [Wnioski](#wnioski)
    3. [Test](#test)

# Cel: <a name="cel"></a>
Celem przygotowanego rozwiązania jest identyfikacja zachowania użytkownika i klasyfikacja zachowania do jednej z sześciu klas.

# Dane: <a name="dane"></a>
Dane do trenowania modelu znajdują się w pliku `final_train.csv` i zostały dostarczone przez organizatorów.

Zawierają informacje o aktywnościach uczetników biorących udział w eksperymencie. Zbiór danych składa się z sześciu podstawowych czynności: trzech postaw statycznych (stanie, siedzenie, leżenie) oraz trzech czynności dynamicznych (chodzenie, schodzenie po schodach i wchodzenie po schodach). Podczas wykonywania eksperymentu wszyscy uczestnicy nosili przypięty na pasku smartfon (Samsung Galaxy S II). 

Przechwytywano 3-wymiarowe przyspieszenie liniowe i 3-wymiarową prędkość kątową w stałej częstotliwości 50Hz przy użyciu wbudowanego w urządzenie akcelerometru i żyroskopu.

Uzyskany zbiór danych został losowo podzielony na dwa zestawy, gdzie zbiór treningowy zawiera 75% danych, a 25% danych to zbiór testowy.

# Rozwiązanie: <a name="rozwiazanie"></a>

## Modele: <a name="modele"></a>
Przygotowaliśmy 3 różne modele, które rozwiązują zadany problem.

Rozwiązania znajdują się w folderach:
[Pierwszy model](https://github.com/pfilo8/BHL-Hackathon-AI/tree/master/results/3categories)
[Drugi model](https://github.com/pfilo8/BHL-Hackathon-AI/tree/master/results/prunned_tree)
[Trzeci model](https://github.com/pfilo8/BHL-Hackathon-AI/tree/master/results/automl-single-model-2021-28-09-21-28-03)

**Pierwszy model** to drzewo decyzyjne, które charakteryzuje 100% skuteczność w rozdzielaniu aktywności na 3 klasy: 
* siedzenie i stanie,
* leżenie,
* chodzenie.
Jest **najprostszy i najłatwiejszy w interpretacji**. Jego ogromną zaletą jest szybkość działania i zmniejszona do minimum ilość danych jakich używamy do predykcji (tylko 2 zmienne).

**Drugi model** to drzewo decyzyjne, które rozdziela aktywności na 5 klas ze skutecznością ok. 92%, ale dzięki zastosowaniu mechanizmu przycinania jest w stanie uzyskać **bardzo wysoką skuteczność wnioskując na podstawie tylko 5 zmiennych**.

**Trzeci model** to SVM wytrenowany przy użyciu AutoML, którego decyzje zostały przez nas wyjaśnione dzięki użyciu XAI-a (Explainable Artificial Intelligence).

Charakteryzuje go **bardzo wysoka skuteczność**, najlepsza spośród stworzonych przez nas rozwiązań.

Dzięki zastosowaniu AutoML jesteśmy w stanie w efektywny sposób wybrać **najlepszy algorytm uczenia maszynowego wraz z optymalnym sposobem przetwarzania surowych danych**. Zrozumienie decyzji jest możliwe dzięki wyjaśnieniu modelu (nie używamy go na zasadzie  *"czarnej skrzynki"*).

## Wnioski: <a name="wnioski"></a>
Notatnik `Summary.ipynb` zawiera analizę, porównanie i wnioski wszystkich przygotowanych przez nas rozwiązań.

## Uruchomienie modelu na danych testowych: <a name="test"></a>
W notatniku `Submission.ipynb` można uruchomić zbiór testowy `test_data.csv`. Testuje od dokładność naszego najslepszego modelu.


