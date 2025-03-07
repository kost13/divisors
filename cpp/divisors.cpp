//project: Divisors
//author: Lukasz Kostrzewa

#include <vector>

#define BOOST_PYTHON_STATIC_LIB

#include <boost/python.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>

namespace py = boost::python;

/// compute divisors for the given number
std::vector<int> get_divisors(int num){
    if(num < 1){
        return {};
    }

    std::vector<int> divisors;
    for(int i = static_cast<int>(sqrt(num)); i > 0; --i ){
        if(num % i == 0){
            divisors.push_back(i);
            auto other = num / i;
            if(other != i){
                divisors.push_back(other);
            } 
        }        
    }
    return divisors;
}

/// convert standard vector to python list
py::list vec_to_py_list(const std::vector<int> &v){
    py::list l;
    for(auto n : v){
        l.append(n);
    } 
    return l;
}

/// divisors computations adjusted to python
py::list compute_divisors(int num){
    return vec_to_py_list(get_divisors(num));
}

BOOST_PYTHON_MODULE(divisors)
{    
    py::def("compute_divisors", compute_divisors);
}
