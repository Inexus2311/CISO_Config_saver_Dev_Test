# CCNA Config_saver Python Script

## Version 1.1.0

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/Inexus2311)

#### Script to back up switch configuration files based on a generated list

> The user must provide a destination path as well as the list from which to extract the names of the switches used to save the configurations.

## Features

- Fast backup of configuration files via TACACS of multiple switches
- Automatic backup on Linux environments
- Manual or argumentative input of the target path and the switch list
- Checking SQL Injections and bad Characters and close the program directly
- Checking runing-config is available on target host

# Help

> usage: python3 Config_save.py [-sd Savedirectory][-sw_list switch_list + file extension]

| Commands   | Description                          |
| ---------- | ------------------------------------ |
| -h, --help | help message                         |
| -sd        | target path to save your config_file |
| -sw_list   | switch_list with switch_name         |

# Examples

#### default Mode

```sh
python3 Config_saver.py
```

#### argumentative Mode

```sh
python3 Config_saver.py -sd /home/user/temp -sw_list switch_list.txt
```

## Installation

Requires [python3](https://www.python.org/downloads/) version

## License

**Free Software**
