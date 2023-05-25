# wafapps
Miscellaneous Python scripts for manipulating AWS Well-Architected assessments using boto3.

### AWS WAT Workshop

There is an AWS workshop that has some more mature scripts here: 
[AWS Well Architected Labs - Well Architected Tool](https://www.wellarchitectedlabs.com/well-architectedtool/)

The main missing functionality in the AWS labs is the ability to import from the XLSX, vs using the JSON output, to simplify initial input collection from the customer.

This repository includes the two python scripts from the lab:
<pre>exportAnswersToXLSX.py
exportImportWAFR.py</pre>

They are pretty self explanatory; the workshop site also has good docs and examples.
### wafapps scripts
These scripts are used to export an XLS from an assessment, edit the responses in the XLS by putting X or NA in the "X or NA" column and notes in the Notes column, and then load back into AWS. It will create the assessment (with either the default name or a specfied name) and use the supplied XLS file. It uses <code> openpyxl</code> as the formatting library, which is extensively documented online.

There are three modules:

* **wafnav/questionnaire.py**: meant to be run from the command line. Usage is as follows:
    * `questionnaire.py`<br />
    * `[-h]`: help
    * `[--loglevel {DEBUG,WARNING,INFO,ERROR,CRITICAL}]`: log level. Default is `ERROR`.<br \>
    * `--wlname [WLNAME]`: name for the workload, or "stdout" to emit pipe-delimited test
    * `{gen,parse}`: the command; gen creates (or finds existing) workload with WLNAME and writes XLS;
    * `[xls_file]`: the name to use for the file`
    

* **wafnav/workload.py**: commands to manage a WAF workload
* **wafnav/lens.py**: commands to format pipe-delimited or XLSX output for a designated workload and lens

#### Caveats:
* `Questionnaire.py` is a convenience to allow the use of a formatted XLS to collect input from the customer more simply than with a web app or other contrivance, and then load it back into AWS. Limitations are as follows:
    * The XLS dump and load script relies on hidden columns and defined numeric positions for question_id and choice_id to get the parameters for the load command. If you change the column order or the number of columns, you'll break the script.
    * The script also assumes that the choices are grouped to the corresponding question. If you sort the rows differently you'll break the script.
* Since you're running these tools from the command line, boto3 is using the AWS context you have set up for the CLI tools. Make sure the account, region, etc. is what you expect before running.