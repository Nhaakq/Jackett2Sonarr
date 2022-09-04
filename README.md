# Jackett2Sonarr V1.0

## About / Synopsis

* This Project is a simply **Python3** script for import Indexers from Jackett to Sonarr.
* For the moment, the Script will Import **Newznab** Torrent Prodiver.
* Project status: working
* Feel free to request.

## Table of contents

Use for instance <https://github.com/ekalinin/github-markdown-toc>:

> * [Title / Repository Name](#title--repository-name)
>   * [About / Synopsis](#about--synopsis)
>   * [Table of contents](#table-of-contents)
>   * [Installation](#installation)
>   * [Usage](#usage)
>   * [License](#license)

## Installation

Go on your server and git clone the project :
    ```git clone https://github.com/Nhaakq/Jackett2Sonarr.git```

You need **Python3** Installation: 
The Specific Python modules used in this script are :
* sqlite3
* json

## Usage
At First, you have to configure all the Indexers in your Jackett UI with all the Indexers you want.
- Then launch the Script with python like ```python3 Jackett2Sonarr.py```
    - Sonnar.db path ? : ```Enter the path to your Sonarr Configuration directory.```
    - Jackett configuration path ?  : ```Enter the path to your Jackett Configuration directory.```
    - Do you want to import all Indexers ? (y/n) : ```Press Y or N if you want detailled importation or not ...```
- Then, The script will prompt you the List of Indexers Configured in Jackett.
- If you pressed **Y** to the previous question, the script will **add** all Indexers and **Update** Indexers already existing (*with the same name*)
- If you pressed **N** :
    - Enter the Indexers number separate with spaces :```Exemple : '10 2 1' ```
- Then the script will **add** all Indexers and **Update** Indexers already existing (*with the same name*)


## Contributing / Reporting issues

* [Link to Issues](https://github.com/Nhaakq/Jackett2Sonarr/issues/new)
* [Link to project](https://github.com/Nhaakq/Jackett2Sonarr)

## License

[Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/)

## THANKS / AUTHORS
 [@Nhaakq] (https://www.github.com/Nhaakq)
