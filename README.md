# Resume parser
![](https://github.com/Zummit-Africa-Inc/resumeparser_api/blob/main/resume-parsing_diagram.png)
With this API, users/companies can take a resume as an input, which can be in PDF or MS Word format, and convert it into a structured JSON data format.


```
# Features

- Extract name
- Extract email
- Extract mobile numbers
- Extract skills
- Extract total experience
- Extract college name
- Extract degree
- Extract designation
- Extract company names

```

# Installation

- You can install this package using

```bash
pip install resume_parser
```

# Supported File Formats

- PDF and DOCx and TXT files are supported on all Operating Systems

# Usage

- Import it in your Python project

```python
from resume_parser import resumeparse

data = resumeparse.read_file('/path/to/resume/file')
```

For first time it will take around a minute so please keep patience.

# Result

The module would return a dictionary with result as follows:

```
{'degree': ['BSc','MSc'],
     'designition': [
         'content writer',
         'data scientist',
         'systems administrator',
     ],
     'email': 'firstnamelastname@gmail.com',
     'name': 'Ada Lovelace',
     'phone': '+232222222',
     'skills': [
         'Python',
         ' C++',
         'Power BI',
         'Tensorflow',
         'Keras',
         'Pytorch',
         'Scikit-Learn',
         'Pandas',
         'NLTK',
         'OpenCv',
         'Numpy',
         'Matplotlib',
         'Seaborn',
         'Django',
         'Linux',
         'Docker'],
     'total_exp': 3,
     'university': ['Harvard University', 'Yale university', 'Howard university']}
```

[<img alt="alt_text"  src="coffee.png" />](https://www.payumoney.com/paybypayumoney/#/147695053B73CAB82672E715A52F9AA5)
