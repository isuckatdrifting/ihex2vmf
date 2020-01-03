# ihex2vmf
Python script for converting Intel Hex memory file to Micron VMF

Example Usage -- Intel Hex to VMF

`Python3 ihex2vmf.py ./example/hello.hex ./example/hello.vmf`

Micron VMF format example
```
@8000 // @hex_address
76 // hex_data_0
34 // hex_data_1

@8008
54
```
If you found that this repo is re-inventing a wheel, please ping me by posting an issue.

## Reference
- [Wikipedia/Intel HEX format](https://en.wikipedia.org/wiki/Intel_HEX)