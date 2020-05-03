#include <vector>
#include <boost/python.hpp>

using namespace boost::python;

std::vector<int> compute_divisors(int num){
    return std::vector<int>(5, num);
}

BOOST_PYTHON_MODULE(divisors)
{
    def("compute_divisors", compute_divisors);
}
