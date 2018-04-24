import io
import unittest

from bddrest.story import Story


class DocumentaryTestCase(unittest.TestCase):
    sample_yaml = '''
        base_call:
          as_: visitor
          title: Quickstart!
          description: Awesome API!
          url: /books/:id
          url_parameters:
            id: '1'
          query:
            a: 1
            b: '2'
          verb: PUT
          form:
            f1: abc
            f2: 123
          headers:
            - 'Content-Type: application/json;charset=utf-8'
          response:
            headers:
            - 'Content-Type: application/json;charset=utf-8'
            json:
              foo: bar
            status: 200 OK
        calls:
        - response:
            headers:
            - 'Content-Type: text/plain;charset=utf-8'
            status: 404 Not Found
          title: Trying invalid book id
          description: trying an invalid book id.
          url_parameters:
            id: None
          query:
            a: 2
            b: 4
          headers:
          - 'A: B'
          form:
            f1: cba
    '''
    def test_markdown(self):
        story = Story.loads(self.sample_yaml)
        outfile = io.StringIO()
        story.document(outfile)
        outputstring = outfile.getvalue()
        self.maxDiff = None
        self.assertEqual('''\
## Quickstart!

### PUT /books/:id

Awesome API!

### Url Parameters

Name | Example
--- | ---
id | 1

### Query Strings

Name | Example
--- | ---
a | 1
b | 2

### Form

Name | Example
--- | ---
f1 | abc
f2 | 123

### Request Headers

* Content-Type: application/json;charset=utf-8

### Response: 200 OK

#### Headers

* Content-Type: application/json;charset=utf-8

#### Body

```json
{"foo": "bar"}
```

## WHEN: Trying invalid book id

trying an invalid book id.

### Url Parameters

Name | Example
--- | ---
id | None

### Query Strings

Name | Example
--- | ---
a | 2
b | 4

### Form

Name | Example
--- | ---
f1 | cba

### Request Headers

* A: B

### Response: 404 Not Found

#### Headers

* Content-Type: text/plain;charset=utf-8

''',
            outputstring
        )


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
