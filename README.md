# MOK notes

- business finland data 2015-2022 selected from https://tietopankki.businessfinland.fi/anonymous/extensions/MaksettuRahoitus/MaksettuRahoitus.html

- download Finnish founded companies 2015-2019
```commandline

# after PRH stomps giving data, check csv file, last row , start loading again with updated datetime
cd ~/git/Omat/HankenKandi/finnish_business_portal/finnish_business_portal/tasks/
python getcompanies.py --year 2015 --month 11 --day 10
# results in ~/git/Omat/HankenKandi/finnish_business_portal/data

```
- once we know y-code one can count how many financial statements there has been
  (is the company really alive???)

# Finnish Business Portal

> Python interface for PRH corporate data

> Open Data, Python 3

---

## Features
-  Query data using simple syntax
-  Complete access to the APIs and parameters provided by PRH

### Upcoming Features
-  Load query parameters from Excel file
-  Generate template for query parameters
-  Default queries for addresses, contact details et cetera

### Possible Features
- Graphical User Interface

---

## Prerequisites

```
Python 3
Pandas
Requests
```

## Example

> Querying the API for companies named _Nokia_ and _Fortum_ that are registered after year 2000
```python
import finnish_business_portal as busportal

# Selecting BisCompany API
portal = busportal.SearchModel("BisCompany")
portal.search(name=["fortum", "nokia"], company_registration_from="2000-01-01")

portal.to_frame().results
```

<br>

> Getting all available APIs
```python
busportal.api_infos
```

> and parameters
```python
busportal.SearchModel("BisCompany").parameter_infos
```


<br>

> Querying all information and saving to Excel:
```python
portal = busportal.SearchModel("BisCompany", loop_results=True, deep=True)
portal.search(name=["fortum", "nokia"], company_registration_from="2000-01-01")

portal.to_frame().results.to_excel("mydata.xlsx")
```

<br>

> Please see [Demo](demo.ipynb) for thorough examples

---

## Author

* **Mikael Koli** - [Miksus](https://github.com/Miksus) - koli.mikael@gmail.com

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
