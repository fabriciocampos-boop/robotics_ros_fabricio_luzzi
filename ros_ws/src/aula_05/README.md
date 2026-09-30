# Aula 05 - Parâmetros e Launch Files

## Subtema

Implementação de parâmetros e Launch Files no ROS 2 para configurar e executar múltiplos nós de forma integrada.

- **`cylinder_area`:** Criar um nó em C++ que recebe o raio do cilindro através do parâmetro `radius`, calcula a área da base e publica o resultado em um tópico.
- **`cylinder_volume`:** Criar um nó em Python que recebe a área da base, utiliza o parâmetro `height` para calcular o volume do cilindro e publica o resultado.
- **`cylinder_bringup`:** Criar Launch Files para iniciar os nós de área e volume juntos, configurar parâmetros, carregar arquivos YAML, realizar remapeamentos de tópicos e organizar a execução do sistema.

## Atividades

- [`cylinder_area`](<cylinder_area>)
- [`cylinder_bringup`](<cylinder_bringup>)
- [`cylinder_volume`](<cylinder_volume>)