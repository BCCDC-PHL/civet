![](./doc_figures/website_header.png)

# Input options

How to investigate an outbreak using civet

### -i / --input

<strong>civet</strong> automatically detects a number of different inputs:

<strong>config.yaml</strong>

A yaml (or yml) config file that describes the analysis you want to run and the type of report you want to generate.

You can provide any of the command line arguments via this config file, for instance pass the input.csv or ID string in through via the configuation file.

Using this input option will allow the user to run very specific, elaborate reports again and again, without having to specify all arguments via the command line.

Note, if the same option is specified in the config file and as a command line argument, the command line argument will overwrite the config file option. 
```
civet -i config.yaml
```

Example config.yaml file:

```
# Input options:
query: test.csv
fasta: test.fasta

# Output options:
output_prefix: outbreak001
safety_level: 1 
# Anonymises background COG-IDs 
# but shows adm2

# Tree options:
distance: 2
protect: adm2=Edinburgh


# Customise the report:
sequencing-centre: EDIN 
title: Outbreak 001 Report
report_date: 2020-08-01 
authors: Verity, Aine
omit_appendix: True
tree_fields: adm1,HCW_status
colour_by: adm1:viridis,HCW_status:Paired
label_fields: [name, sample_date]

```

<strong>input.csv</strong>

Input csv file with an identifier column. By default <strong>civet</strong> will look for a column called `name` but this can be changed with the `--input-column` flag (or added to the input config file).

Example csv:
| name | status | adm2 | 
| --- | --- | --- |
| sample1 | HCW | Edinburgh | 
| sample2 | HCW | Edinburgh | 
| sample3 | Patient | Edinburgh | 
| sample4 | HCW | Edinburgh | 

Either:
1) Run: ``civet -i input.csv``
or
2) Specify ``query: input.csv`` in the config.yaml file and run ``civet -i config.yaml``

<strong>ID string</strong>

A comma separated string of ids that civet trys to match against the database (you can define what field you want to match against with `--data-column`, the default is will match against the COG-UK ID).

Either:
1) Run: ``civet -i EGID001,EGID002``
or
2) Specify ``ids: EGID001,EGID002`` in the config.yaml file and run ``civet -i config.yaml``


### -fm / --from-metadata

If all sequences of interest are in the background tree and metadata, the user can opt to define a set of query sequences using the ``--from-metadata`` flag. 

To do this, supply one or more of ``column_name=match_string`` pairs. For example:
```
civet -fm adm2=Edinburgh sample_date=2020-09-20
```

civet can also detect and filter by date ranges:
```
civet -fm sample_date=2020-05-01:2020-06-01
```

A <strong>civet</strong> instance is then run with the sequences that match the search parameters.



### -p / --protect

In the same ``column_name=match_string`` pair format as the `--from-metadata` search, the user can protect certain sequences from being collapsed in the report. 

For example:
```
civet -i input.csv -p adm2=Edinburgh sample_date=2020-09-01:2020-10-01
```
runs a civet report using the input specified in input.csv, but any sequences from Edinburgh in September that are present in the local trees will be displayed and not collapsed.

### -f / --fasta

Optional input fasta file with sequences not yet added to the background data. These will be added into the tree next to their closest sequence found in the background data.

<strong>--max-ambiguity</strong> 
Maximum proportion of Ns allowed to attempt analysis. Default: 0.5 (i.e. 50% N content)

<strong>--min-length</strong>
Minimum query length allowed to attempt analysis. Default: 10000


### --generate-config
The yaml file can be created manually or can be generated by runnnig civet with the set of command line arguments you want to specify in conjunction with the `--generate-config` flag. 

It will not run the analysis, but will produce a template config.yaml file that you can use again and again. 


### [Next: Background data](./background_data.md)