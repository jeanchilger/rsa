# RSA Cryptosystem

Implementation of RSA cryptosystem in python. This may not be a safe, production-ready implementation. Developed for learning purposes.

## Installing

First, clone this repository:

```
git clone https://github.com/jeanchilger/rsa.git
cd rsa
```

Them, install the required python dependencies:

```
pip install -r requirements.txt
```

This tool was created and tested using `python 3.9.7`

## Running

This tool was created as a CLI-based [Typer](https://typer.tiangolo.com/) application. The entry point of application is the `main.py` file, at the root folder: 

```
python main.py COMMAND [ARGS]
```

You can also type `python main.py --help` to see usage instructions, or `python COMMAND --help` to display help for a specific command.

### Commands

In this section, a brief explanation of the available commands is given. Additionally, we provide an [end-to-end example](https://github.com/jeanchilger/rsa/blob/master/usage-guide.md) of their usage.

#### `init`

Initializes a new "environment" - a local place to keep configurations. No options or arguments available.

```
python main.py init
```

#### `env`

Provides access to the "environment".

```
python main.py env COMMAND [ARGS]
```

#### `encrypt`

Encrypts a text accordingly to RSA rules.

```
python main.py encrypt SRC [OPTIONS]
```

`SRC` is the source text to be encrypted. If a path to a file is provided, the contents of that file are used.

The available options are:

* `--dest PATH`: Path to file where encryptation should be stored. If omitted, result will be written to stdout.
* `--pkey TEXT`: Public key to be used for encryptation. If omitted, the public key from environment will be used.
* `--help`: Shows a help message.


#### `decrypt`

Decrypts a text cyphered with RSA.

```
python main.py decrypt SRC [OPTIONS]
```

`SRC` is the source text to be decrypted. If a path to a file is provided, the contents of that file are used.

The available options are:

* `--dest PATH`: Path to file where decryptation should be stored. If omitted, result will be written to stdout.
* `--pkey TEXT`: Private key to be used for decryptation. If omitted, the private key from environment will be used.
* `--help`: Shows a help message.

## File structure

The main features are inside `src/` folder. The `commands/` folder gather larger subcommands. The `utils/` folder contains utility and helper minor functions.

## License

This project is licensed under the MIT license. See [LICENSE](https://github.com/jeanchilger/rsa/blob/master/LICENSE) for more information.
