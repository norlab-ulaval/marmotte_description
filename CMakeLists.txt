cmake_minimum_required(VERSION 3.8)
project(marmotte_description)

find_package(ament_cmake REQUIRED)
find_package(urdf REQUIRED)
find_package(xacro REQUIRED)

# Install
foreach(dir launch materials meshes sdf urdf)
install(DIRECTORY ${dir}
    DESTINATION share/${PROJECT_NAME})
endforeach(dir)
    
ament_package()
