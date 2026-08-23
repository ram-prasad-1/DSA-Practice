`
Whenever any code is run in JavaScript, it’s run inside an abstract environment called execution context.

Phases of the JavaScript Execution Context
- Creation Phase: Execution Context is created,
                  all the variables are stored in the memory
                  and scope chain is created
- Execution Phase: execute the code and thereafter destroy the context.

2 types of execution context:
- global
- functional
  - Created each time a function is invoked.
  - The arrow function doesn't define its own execution context
    but resolves to the one from the outer function.

Call Stack:
To keep the track of all the contexts the JavaScript engine uses a call stack.

When the engine first starts executing the script,
it creates a global context and pushes it on the stack.

When execution of the current function is complete,
then the JavaScript engine will automatically
remove the context from the call stack and it goes back to its parent.

`;
