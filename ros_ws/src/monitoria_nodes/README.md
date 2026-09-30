# Monitoria - Nodes

## Subtema

Treinamento prático dos conceitos de criação, comunicação e execução de nós no ROS 2.

- **`sum_vector.cpp`:** Criar um nó em C++ que recebe dois vetores através da mensagem customizada `TwoVector`, realiza a soma de suas componentes e publica o vetor resultante.

- **`process_number_node.py`:** Criar um nó em Python que recebe um número pelo tópico `input`, multiplica seu valor por 2 e publica o resultado no tópico `result`.

- **`div_number_node.py`:** Criar um nó em Python que recebe um número pelo tópico `input`, divide seu valor por 2 e publica o resultado no tópico `div_number`.

- **`TwoVector.msg`:** Criar uma mensagem customizada para transportar dois vetores entre os nós.

- **`number.launch.py`:** Criar um Launch File para executar os nós da monitoria em conjunto.

## Atividades

- [`launch/number.launch.py`](<launch/number.launch.py>)
- [`msg/TwoVector.msg`](<msg/TwoVector.msg>)
- [`scripts/div_number_node.py`](<scripts/div_number_node.py>)
- [`scripts/process_number_node.py`](<scripts/process_number_node.py>)
- [`src/sum_vector.cpp`](<src/sum_vector.cpp>)