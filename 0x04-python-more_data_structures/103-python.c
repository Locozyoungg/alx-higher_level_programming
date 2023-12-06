#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    PyVarObject *var = (PyVarObject *)p;
    ssize_t size, allocated, i;
    PyObject *obj;

    printf("[*] Python list info\n");
    size = var->ob_size;
    allocated = list->allocated;
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; ++i)
    {
        obj = list->ob_item[i];
        printf("Element %ld: %s\n", i, obj->ob_type->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    PyVarObject *var = (PyVarObject *)p;
    ssize_t size, i;

    printf("[.] bytes object info\n");
    size = var->ob_size;
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes->ob_sval);
    printf("  first 10 bytes:");

    for (i = 0; i < size && i < 10; ++i)
        printf(" %02hhx", bytes->ob_sval[i]);

    printf("\n");
}
