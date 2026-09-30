import rclpy
from rclpy.node import Node

class MeuNo(Node):
    def __init__(self):
        super().__init__('meu_no')

        # Declara os parâmetros com valores padrão
        self.declare_parameter('nome', 'robo1')
        self.declare_parameter('velocidade', 1.0)
        self.declare_parameter('ativo', True)

        # Lê os valores (podem vir do launch file, YAML ou linha de comando)
        nome = self.get_parameter('nome').get_parameter_value().string_value
        velocidade = self.get_parameter('velocidade').get_parameter_value().double_value
        ativo = self.get_parameter('ativo').get_parameter_value().bool_value

        self.get_logger().info(f'Nome: {nome}, Velocidade: {velocidade}, Ativo: {ativo}')

        # Timer para reagir a mudanças de parâmetro em tempo real (opcional)
        self.add_on_set_parameters_callback(self.callback_parametros)

    def callback_parametros(self, params):
        for param in params:
            self.get_logger().info(f'Parâmetro alterado: {param.name} = {param.value}')
        from rcl_interfaces.msg import SetParametersResult
        return SetParametersResult(successful=True)


def main(args=None):
    rclpy.init(args=args)
    no = MeuNo()
    rclpy.spin(no)
    no.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()