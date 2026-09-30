cmake_minimum_required(VERSION 3.8)
project(monitoria_nodes)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# dependências
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/TwoVector.msg"
  DEPENDENCIES geometry_msgs # Add packages that above messages depend on, in this case geometry_msgs for Sphere.msg
)


add_executable(teste src/teste.cpp)
ament_target_dependencies(teste rclcpp std_msgs)

add_executable(sum_vector src/sum_vector.cpp)
ament_target_dependencies(sum_vector rclcpp geometry_msgs rosidl_default_generators)

rosidl_get_typesupport_target(cpp_typesupport_target
  ${PROJECT_NAME}
  "rosidl_typesupport_cpp"
)

target_link_libraries(sum_vector
  "${cpp_typesupport_target}"
)

install(
  TARGETS teste sum_vector
  DESTINATION lib/${PROJECT_NAME}
)

# scripts Python
install(
  PROGRAMS
    scripts/process_number_node.py
    scripts/div_number_node.py
  DESTINATION lib/${PROJECT_NAME}
)

# launch files
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()