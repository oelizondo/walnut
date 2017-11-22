## Walnut Compiler

### Compile Grammar

```console
antlr4 -Dlanguage=Python2 compiler/walnut.g4
```

### Run

```console
cd compiler
python main.py main.walnut
```

Using the CLI

```console
$ walnut compile example.walnut
$ walnut run
```

Installing

```console
$ curl -L https://raw.githubusercontent.com/oelizondo/walnut/master/install.sh | sh
```

### Todo

* ~~Call a function~~
* ~~Declaration (of independence) and Assignment (at the same time)~~
* Translate variables to memory addresses.
* Start VM
