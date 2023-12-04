#include <Python.h>

void print_python_list_info(PyObject *p)
{
    long int size = PyList_Size(p);
    int i;

    printf("[*] Size of the Python List = %li\n", size);

    if (PyList_Check(p))
    {
        PyListObject *obj = (PyListObject *)p;
        printf("[*] Allocated = %li\n", obj->allocated);

        for (i = 0; i < size; i++)
        {
            printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
        }
    }
}
