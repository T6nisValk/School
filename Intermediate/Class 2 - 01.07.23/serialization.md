# Serialization

Serialization is the process of converting structured data to a format that allows for storage and sharing. Save as flat or nested.

- File, escpecially csv - flat data
- Pickle - nested data
- JSON - nested data
- Numpy array - flat data
- XML - nested data
- YAML - nested data

## Pickle

This is a native serialization module in python. Pickling is the process whereby a pyhon object hierachy is converted into a byte stream.

Pickle is not secure against erroneous or malicious constructed data. `NEVER` unpickle data recieved from an untrusted or unauthanticated source.