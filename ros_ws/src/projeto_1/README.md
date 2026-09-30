# Projeto 01 - Publisher e Subscriber

## Subtema

Desenvolvimento de um nó em C++ no ROS 2 para controlar o movimento de um robô até um objetivo utilizando comunicação por tópicos.

- Receber a posição desejada pelo tópico `/goal` utilizando `geometry_msgs/msg/Vector3`.
- Receber a posição atual do robô pelo tópico `/robot_position` utilizando `geometry_msgs/msg/Pose`.
- Calcular as velocidades linear e angular necessárias para conduzir o robô até o objetivo.
- Publicar os comandos de velocidade no tópico `/cmd_vel` utilizando `geometry_msgs/msg/TwistStamped`.
- Publicar os comandos a uma frequência de 10 Hz e manter o robô parado enquanto nenhum objetivo for recebido.

## Atividades

- [`Pacote do Projeto`](<velocity_controller>)