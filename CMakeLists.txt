cmake_minimum_required(VERSION 3.8)
project(marmotte_description)

find_package(ament_cmake REQUIRED)
find_package(urdf REQUIRED)
find_package(xacro REQUIRED)

install(DIRECTORY launch
    DESTINATION share/${PROJECT_NAME})

install(DIRECTORY urdf
    DESTINATION share/${PROJECT_NAME})

install(DIRECTORY new_urdf_01-16-2023
	DESTINATION share/${PROJECT_NAME})
    
ament_package()
