# Hackathon 03 - System Monitor

## Subtema

Desenvolvimento de um sistema de monitoramento do computador embarcado utilizando ROS 2 e mensagens customizadas.

- **`system_monitor_interfaces`:** Criar mensagens customizadas para organizar informações de CPU, memória RAM e armazenamento, incluindo uma mensagem principal com `Header` e submensagens específicas para cada recurso.

- **`system_monitor`:** Implementar um nó em Python utilizando a biblioteca `psutil` para coletar periodicamente informações do computador, preencher as mensagens customizadas e publicar o estado do sistema em um tópico ROS.

## Atividades

- [`system_monitor_interfaces`](<system_monitor_interfaces>)
- [`system_monitor`](<system_monitor>)