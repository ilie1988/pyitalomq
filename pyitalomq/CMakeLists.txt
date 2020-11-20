
pybind11_add_module(pyitalomq MODULE
  bencode.cpp
  italomq.cpp
  module.cpp
)

target_link_libraries(pyitalomq PUBLIC italomq::italomq)


