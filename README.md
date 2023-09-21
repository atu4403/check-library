# Check

## Overview

The Check library is a Python-based assertion framework designed to simplify the validation process in tests. It offers a wide range of assertion methods that provide clear and informative failure messages.

## Features

* Comprehensive set of assertion methods for different data types and structures.
* Support for custom failure messages to improve debugging.
* Easy-to-understand method naming for better code readability.
* Minimalistic and lightweight design for quick integration into any project.

## Installation

You can install the Check library via pip:

```bash
pip install che
```

## Quick Start

Here is a simple example demonstrating some of the assertion methods:

```python
from che import Check

# Initialize the Check instance
check = Check()

# Perform assertions
check.equal(1, 1)
check.notEqual(1, 2)
check.isAbove(2, 1)

# Validate the number of assertions made
check.assert_calls(3)
```

## Documentation

For more detailed information on using the Check library, please refer to the official documentation.

[Check Docs](https://atu4403.github.io/check-library)
