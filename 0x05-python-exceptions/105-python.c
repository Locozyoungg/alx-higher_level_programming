#include <Python.h>

/**
 * print_python_float - Prints basic info about Python floats.
 * @p: A PyObject float.
 */
void print_python_float(PyObject *p)
{
    double value;

    printf("[.] float object info\n");

    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);

    printf("  value: %.16g\n", value);
}
