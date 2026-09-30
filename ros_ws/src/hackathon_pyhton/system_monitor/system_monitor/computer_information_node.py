import rclpy
from rclpy.node import Node
from system_monitor_interfaces.msg import AllInformationComputer, CpuMessage, DiscoMessage, RamMessage
import psutil

class ComputerInformation(Node):
    def __init__(self):
        super().__init__("computer_information_node")
        self.publisher = self.create_publisher(AllInformationComputer, "/topico_name", 10)
        self.timer_publisher_ = self.create_timer(1.0, self.timer_callback)


    def timer_callback(self):

        cpu = CpuMessage()
        #Número de cores do processador
        cpu.number_cores = len(psutil.Process().cpu_affinity())
        #Porcentagem média de uso da CPU 
        cpu.mean_use_percentage = psutil.cpu_percent(interval=None,percpu=False)
        #Porcentagem de uso individual de cada core
        cpu.mean_use_core_percentage = psutil.cpu_percent(interval=None,percpu=True)

        #Maior temperatura da CPU em graus Celsius
        temperaturas = []
        max_temp = 0
        for indice in psutil.sensors_temperatures().keys():
            temperaturas.append(psutil.sensors_temperatures()[indice][0].current)
            max_temp = 0
        for temp in temperaturas:
            if temp > max_temp:
                max_temp=temp
        cpu.temperature = max_temp

        ram = RamMessage()
        ram.use_percentage = psutil.virtual_memory()[2]
        ram.total_memory_bytes = psutil.virtual_memory()[0]
        ram.use_memory_bytes = psutil.virtual_memory()[3]
        disco = DiscoMessage()

        disco.use_disco_percentage = psutil.disk_usage('/')[3]
        disco.total_disco_bytes = psutil.disk_usage('/')[0]
        disco.use_disco_bytes = psutil.disk_usage('/')[1]

        all_info = AllInformationComputer()
        all_info.cpu = cpu
        all_info.disc = disco
        all_info.ram = ram

        self.publisher.publish(all_info)
        return

    
def main(args=None):
    rclpy.init(args=args)
    node = ComputerInformation()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()