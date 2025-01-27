![](./doc_figures/website_header.png)


# Usage
How to investigate an outbreak using civet

### Input files

Find detailed information about input file options <a href="{{ 'input_options.md' | absolute_url }}">here</a>. 

In brief, either provide an input csv file, an ID string or a config yaml file via the ``-i / --input`` option. 

Alternatively, define a search criteria with ``-fm / --from-metadata``. 

### Input background data

<strong>civet</strong> summarises information around a set of sequences of interest. It relies on the user providing a background tree, alignment and metadata file. <strong>civet</strong> can be run on CLIMB with the ``--CLIMB`` flag, remotely with the ``-r / --remote`` flag or locally by specifying a local directory. If no options are given, civet will automatically look for a directory called `civet-cat` in the current working directory.

Find detailed information about background data options <a href="{{ 'background_data.md' | absolute_url }}">here</a>. 

The data files <strong>civet</strong>  looks for are:
```
cog_global_alignment.fasta
cog_global_metadata.csv
cog_global_tree.nexus
```

### Running civet

1. Activate the environment ``conda activate civet``


2. To run a simple analysis, you can input your prefered options via the command line. Run:

```
civet -i input.csv -f input.fasta -r -uun <your-user-name>
```
where `<your-user-name>` represents your unique CLIMB identifier.

3. If you're going to be running a similar analysis again and again, a configuration file simplifies the process. The config file can be generated manually, or by running the command line options you require in addition to the `--generate-config` flag.

```
civet -fm adm2=Edinburgh sample_date=2020-10-01:2020-01-05 -d civet-cat -sc EDIN --generate-config
```

Running civet is then simple:
```
civet -i config.yaml
```

### civet config file notes

- Config keys are insensitive to '-' and '_' differences. 
  Example: `--from-metadata` can be added to the config.yaml file as `from_metadata: ` or `from-metadata`
- All command line options are available to be input in the config file other than the following exceptions: 
  input.csv is specified with `query: input.csv` 
  ID string is specified with `ids: EGID001,EGID002`

### Full usage

<strong>input-output options:</strong>

```
-i INPUT, --input INPUT
            Input config file in yaml format, csv file (with
            minimally an input_column header, Default=`name`) or
            comma-separated id string with one or more query ids.
            Example: `EDB3588,EDB3589`.
-fm [FROM_METADATA [FROM_METADATA ...]], 
--from-metadata [FROM_METADATA [FROM_METADATA ...]]
            Generate a query from the metadata file supplied.
            Define a search that will be used to pull out
            sequences of interest from the large phylogeny. E.g.
            -fm adm2=Edinburgh sample_date=2020-03-01:2020-04-01
-o OUTDIR, --outdir OUTDIR
            Output directory. Default: current working directory
-f FASTA, --fasta FASTA
            Optional fasta query.
--max-ambiguity MAX_AMBIGUITY
            Maximum proportion of Ns allowed to attempt analysis.
            Default: 0.5
--min-length MIN_LENGTH
            Minimum query length allowed to attempt analysis.
            Default: 10000
```

<strong>data source options:</strong>

```

-d DATADIR, --datadir DATADIR
            Local directory that contains the data files. Default:
            civet-cat
-m BACKGROUND_METADATA, --background-metadata BACKGROUND_METADATA
            Custom metadata file that corresponds to the large
            global tree/ alignment. Should have a column
            `sequence_name`.
--CLIMB               Indicates you're running CIVET from within CLIMB, uses
            default paths in CLIMB to access data
-r, --remote    Remotely access lineage trees from CLIMB
-uun UUN, --your-user-name UUN
            Your CLIMB COG-UK username. Required if running with
            --remote flag
--input-column INPUT_COLUMN
            Column in input csv file to match with database.
            Default: name
--data-column DATA_COLUMN
            Option to search COG database for a different id type.
            Default: COG-UK ID
```

<strong>report customisation:</strong>

```
-sc SEQUENCING_CENTRE, --sequencing-centre SEQUENCING_CENTRE
            Customise report with logos from sequencing centre.
--display-name DISPLAY_NAME
            Column in input csv file with display names for seqs.
            Default: same as input column
--sample-date-column SAMPLE_DATE_COLUMN
            Column in input csv with sampling date in it.
            Default='sample_date'
--colour-by COLOUR_BY
            Comma separated string of fields to display as
            coloured dots rather than text in report trees.
            Optionally add colour scheme eg adm1=viridis
--tree-fields TREE_FIELDS
            Comma separated string of fields to display in the
            trees in the report. Default: country
--label-fields LABEL_FIELDS
            Comma separated string of fields to add to tree report
            labels.
--date-fields DATE_FIELDS
            Comma separated string of metadata headers containing
            date information.
--node-summary NODE_SUMMARY
            Column to summarise collapsed nodes by. Default =
            Global lineage
--table-fields TABLE_FIELDS
            Fields to include in the table produced in the report.
            Query ID, name of sequence in tree and the local tree
            it's found in will always be shown
--include-snp-table   Include information about closest sequence in database
            in table. Default is False
--no-snipit           Don't run snipit graph
--include-bars        Render barcharts in the output report
--omit-appendix       Omit the appendix section. Default=False
--private             remove adm2 references from background sequences.
            Default=True

```
<strong>tree context options:</strong>
```
--distance DISTANCE   Extraction from large tree radius. Default: 2
--up-distance UP_DISTANCE
            Upstream distance to extract from large tree. Default:
            2
--down-distance DOWN_DISTANCE
            Downstream distance to extract from large tree.
            Default: 2
--collapse-threshold COLLAPSE_THRESHOLD
            Minimum number of nodes to collapse on. Default: 1
-p [PROTECT [PROTECT ...]],
--protect [PROTECT [PROTECT ...]]
            Protect nodes from collapse if they match the search
            query in the metadata file supplied. E.g. -p
            adm2=Edinburgh sample_date=2020-03-01:2020-04-01
```

<strong>map rendering options:</strong>
```
--local-lineages      
            Contextualise the cluster lineages at local regional
            scale. Requires at least one adm2 value in query csv.
--date-restriction   
            Chose whether to date-restrict comparative sequences
            at regional-scale.
--date-range-start DATE_RANGE_START
            Define the start date from which sequences will COG
            sequences will be used for local context. YYYY-MM-DD
            format required.
--date-range-end DATE_RANGE_END
            Define the end date from which sequences will COG
            sequences will be used for local context. YYYY-MM-DD
            format required.
--date-window DATE_WINDOW
            Define the window +- either side of cluster sample
            collection date-range. Default is 7 days.
--map-sequences       Map the sequences themselves by adm2, coordinates or
            otuer postcode.
--map-info MAP_INFO   columns containing EITHER x and y coordinates as a
            comma separated string OR outer postcodes for mapping
            sequences OR Adm2
--input-crs INPUT_CRS
            Coordinate reference system for sequence coordinates
--colour-map-by COLOUR_MAP_BY
            Column to colour mapped sequences by
```

<strong>run options</strong>
```
  --cluster             Run cluster civet pipeline. Requires -i/--input csv
  --update              Check for changes from previous run of civet. Requires
                        -fm/--from-metadata option in a config.yaml file from
                        previous run
  -c, --generate-config
                        Rather than running a civet report, just generate a
                        config file based on the command line arguments
                        provided
  -b, --launch-browser  Optionally launch md viewer in the browser using grip
```

<strong>misc options:</strong>
```
  --safety-level SAFETY_LEVEL
                        Level of anonymisation for users. Options: 0 (no
                        anonymity), 1 (no COGIDs on background data), 2 (no
                        adm2 on data). Default: 1
  --tempdir TEMPDIR     Specify where you want the temp stuff to go. Default:
                        $TMPDIR
  --no-temp             Output all intermediate files, for dev purposes.
  --verbose             Print lots of stuff to screen
  --art                 Print art
  -t THREADS, --threads THREADS
                        Number of threads
  -v, --version         show program's version number and exit
  -h, --help

```

### [Next: Output options](./output.md)