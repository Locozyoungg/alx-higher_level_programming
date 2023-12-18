#include <Python.h>

/**
 * print_python_bytes - Prints basic info about Python bytes.
 * @p: A PyObject bytes.
 */
void print_python_bytes(PyObject *p)
{
    int size, i;
    char *str;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %d\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %d bytes: ", size < 10 ? size + 1 : 10);

    for (i = 0; i < size + 1 && i < 10; i++)
    {
        printf("%02hhx", str[i]);

        if (i < size && i < 9)
            printf(" ");
    }

    printf("\n");
}
