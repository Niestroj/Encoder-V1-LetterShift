# letterShiftEncoder

A simple command-line text encoder and decoder written in Python. It replaces individual characters using a predefined substitution table to make ordinary text less immediately readable.

**This is an obfuscation experiment, not secure encryption.** The substitution rules are visible in the source code and can be reverse-engineered easily. Do not use it to protect passwords, personal information, or other sensitive data.

## Features

- Encode text using a custom character-substitution table.
- Decode text using a corresponding lookup table.
- Enter text interactively in a terminal.
- Preserve spaces and periods during encoding.
- Replace unsupported characters with `█` during encoding.

## Requirements

- Python 3
- No third-party Python packages

The script uses `cls` to clear the console, which is intended for Windows terminals. On other operating systems, the console-clearing command may not work, although the rest of the program may still run.

## Getting started

Clone the repository:

```bash
git clone https://github.com/Niestroj/letterShiftEncoder.git
cd letterShiftEncoder
```

Run the script:

```bash
python "LetterShift-Encoder+Decoder.py"
```

Depending on your system, you may need to use `python3` instead of `python`.

## Usage

The program asks you to choose a mode:

```text
CHOOSE: DECODE OR ENCODE (1/2)
```

- Enter `1` to decode text.
- Enter `2` to encode text.

After selecting a mode, type your text and press Enter. The result is printed in the terminal. The program then returns to the mode-selection prompt.

### Example

Encoding `hello` with the current substitution table produces:

```text
jznnα
```

The program converts input to lowercase before processing it.

## How it works

The encoder processes the input one character at a time. Each supported letter is replaced according to a fixed mapping defined in a series of `if` / `elif` statements. The decoder uses its own mapping to translate encoded characters back into text.

The substitution table includes some nonstandard characters, such as `@`, `ü`, `ä`, and `α` (Greek alpha).

The script also contains code intended to randomly change the case of encoded characters. In its current form, that code calls `.lower()` or `.upper()` without assigning the result, so it does not actually change the output.

## Known limitations

- **Not cryptographically secure:** The mapping is fixed, visible, and straightforward to analyze.
- **Encoding and decoding are not fully reversible:** Some mappings are inconsistent or ambiguous. For example, the encoder maps both `e` and `x` to `z`, so the original character cannot always be recovered.
- **Unsupported input:** During encoding, characters not explicitly supported by the mapping are replaced with `█`, which loses the original character.
- **Case is not preserved:** Input is converted to lowercase.
- **Windows-specific terminal clearing:** The script calls `cls` rather than a cross-platform command.
- **No file processing:** Input and output are handled through the terminal.

## Purpose

This project is a small programming exercise and demonstration of basic Python concepts, including conditional statements, loops, functions, string manipulation, and character substitution. It is intended for experimentation and learning, not for protecting confidential information.

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**. See [LICENSE](LICENSE) for the full license text.

The software is provided without warranty, subject to applicable law and the terms of the license.
