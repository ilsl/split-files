# Just Eat Split Files task

## Introduction

This archive contains all necassary scripts to split a large file based on number of bytes/lines into a smaller file. 

The output files will not exceed the `--max-megabytes` and the `--max-lines` parameters passed to the script. 

## Prerequisites

Python was choosen for this exercise as the programmer had more experiance with this compared with Scala.

  - Python 3.7
  - Bash

## Assumptions

- No tests were needed to be created for this code

## Splitting a file into smaller files

1. Once the files have been unzipped, change your working directory to split-files:
    ```console
    $ cd split-files
    ```

2. To split a file of your choosing based on number of bytes and line number, run as following


        ```console
        $ bash file-splitter.sh --input-file path/to/file --output-dir path/to/dir --max-megabytes 10 --max-lines 2
        ```
## Future TODOs

This coding exercise took 90 minutes. The following future improvements can be made:

 - Add tests for each of the methods
 - add descriptions for each of the methods
 - add types for each of the input arguments for every method
 - Use object oriented programming to streamline code and improve user readability
 - Adhere to PEP8
 
 ## Json to describe programmer
 
 ```
 {
  "fullname": "Isobel Jones",
  "hobbies" : {
    "food" : [
      "eating",
      "cooking", 
      "exploring",
      "++eating",
      "ordering ;)"
      ],
    "sports" : [
      "bouldering",
      "mountain_biking",
      "road_biking",
      "running",
      "hiking"
    ],
    "tech" : {
      "languages" : [
        "python",
        "bash", 
        "groovy", 
        "scala", 
        "hcl"
        ],
        "gaming" : "ps4"
    }
  },
  "passions": [
    "coding",
    "teaching",
    "learning",
    "automation",
    "sun"
    ],
    "weird-habbits": "excessive tea drinker"
}
```
 

