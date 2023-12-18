/* Python.h
   Include file for using the Python API.

   This file includes all other Python header files, so you only need to
   include this one when writing a C extension module.

   Note: If the extension module is intended to be used on different Python
   implementations, you should not use this file directly. Instead, you should
   use the abstract API defined in PEP 384.
*/

#ifndef Py_PYTHON_H
#define Py_PYTHON_H

/* Always include <stdio.h>, since some other headers may depend on it */
#include <stdio.h>

/* Include <limits.h>.  The pyconfig.h file (included from Python.h) may
   or may not define various limit-related macros (e.g. LONG_MAX) and
   <Python.h> may or may not depend on them.  <limits.h> defines them
   reliably.  Note that this must be done *before* including pyport.h,
   because pyport.h may use some of the limits from limits.h. */
#include <limits.h>

/* Include <errno.h> explicitly, because some C libraries don't include
   it in <stdio.h>. */
#include <errno.h>

/* Include the configuration header */
#include "pyconfig.h"

/* Include pyport.h, which defines some portability issues */
#include "pyport.h"

/* Include the core Python headers */
#include "pymacro.h"
#include "pymath.h"
#include "pymem.h"
#include "object.h"
#include "objimpl.h"
#include "typeslots.h"
#include "pyhash.h"
#include "pydebug.h"
#include "bytearrayobject.h"
#include "bytesobject.h"
#include "unicodeobject.h"
#include "longobject.h"
#include "longintrepr.h"
#include "boolobject.h"
#include "floatobject.h"
#include "complexobject.h"
#include "rangeobject.h"
#include "memoryobject.h"
#include "tupleobject.h"
#include "listobject.h"
#include "dictobject.h"
#include "odictobject.h"
#include "enumobject.h"
#include "setobject.h"
#include "methodobject.h"
#include "moduleobject.h"
#include "funcobject.h"
#include "classobject.h"
#include "fileobject.h"
#include "pycapsule.h"
#include "traceback.h"
#include "sliceobject.h"
#include "cellobject.h"
#include "iterobject.h"
#include "genobject.h"
#include "descrobject.h"
#include "warnings.h"
#include "weakrefobject.h"
#include "structseq.h"
#include "namespaceobject.h"
#include "picklebufobject.h"

/* Include the code object and frame object headers */
#include "code.h"
#include "frameobject.h"

/* Include the Python run-time header */
#include "pystate.h"

/* Include the Python thread support header */
#include "pythread.h"

/* Include the Python interpreter header */
#include "ceval.h"

/* Include the Python compiler header */
#include "compile.h"

/* Include the Python symbol table header */
#include "symtable.h"

/* Include the Python module header */
#include "pythonrun.h"

/* Include the Python eval header */
#include "pyeval.h"

/* Include the Python import header */
#include "import.h"

/* Include the abstract object header */
#include "abstract.h"

/* Include the concrete object header */
#include "concrete.h"

/* Include the Python exceptions header */
#include "pyerrors.h"

/* Include the Python signal header */
#include "pysignal.h"

/* Include the Python codecs header */
#include "codecs.h"

/* Include the Python AST header */
#include "Python-ast.h"

/* Include the Python grammar header */
#include "graminit.h"

/* Include the Python profiler header */
#include "pymacconfig.h"

/* Include the Python profiler header */
#include "pyfpe.h"

#endif /* !Py_PYTHON_H */
