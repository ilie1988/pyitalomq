#include "common.hpp"

PYBIND11_MODULE(pyitalomq, m)
{
  italomq::ItaloMQ_Init(m);
  italomq::BEncode_Init(m);
}
